
import json, boto3, numpy as np, io, os, base64, datetime
from PIL import Image
import onnxruntime as ort

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

CLASS_NAMES = ["bacteria", "fungi", "virus"]
MODEL_BUCKET = os.environ['MODEL_BUCKET']
TABLE_NAME = os.environ['DYNAMODB_TABLE']

session = None

def load_model():
    global session
    if session is None:
        tmp_path = '/tmp/model.onnx'
        if not os.path.exists(tmp_path):
            s3.download_file(MODEL_BUCKET, 'models/model.onnx', tmp_path)
        session = ort.InferenceSession(tmp_path)
    return session

def preprocess(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((224, 224))
    arr = np.array(img, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)

def lambda_handler(event, context):
    try:
        image_bytes = base64.b64decode(event.get('body', ''))
        input_data = preprocess(image_bytes)

        sess = load_model()
        input_name = sess.get_inputs()[0].name
        pred = sess.run(None, {input_name: input_data})[0][0]

        idx = int(np.argmax(pred))
        confidence = float(np.max(pred))
        result_class = CLASS_NAMES[idx]

        sorted_p = np.sort(pred)
        gap = float(sorted_p[-1] - sorted_p[-2])
        if confidence < 0.85 or gap < 0.15:
            result_class = "others"

        dynamodb.Table(TABLE_NAME).put_item(Item={
            'prediction_id': context.aws_request_id,
            'timestamp': datetime.datetime.utcnow().isoformat(),
            'result': result_class,
            'confidence': str(round(confidence * 100, 2))
        })

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'result': result_class,
                'confidence': round(confidence * 100, 2),
                'image_url': None
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
