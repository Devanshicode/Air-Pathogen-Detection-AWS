
// ✅ AWS API URL — paste your Invoke URL here + /predict
const API_URL = 'https://xjm9yst8u2.execute-api.us-east-1.amazonaws.com/prod/predict';
 
function captureImage() {
    const fileInput = document.getElementById('imageInput');
    if (!fileInput || !fileInput.files[0]) {
        alert('Please select a microscopy image first');
        return;
    }
    document.getElementById('resultText').innerText = 'Analyzing image...';
    document.getElementById('resultText').className = 'loading';
    const file   = fileInput.files[0];
    const reader = new FileReader();
    reader.onload = async (e) => {
        const base64 = e.target.result.split(',')[1];
        const img    = document.getElementById('previewImage');
        img.src          = e.target.result;
        img.style.display = 'block';
        try {
            const res  = await fetch(API_URL, {
                method: 'POST', body: base64,
                headers: { 'Content-Type': 'text/plain' }
            });
            const data = await res.json();
            if (data.error) {
                document.getElementById('resultText').innerText = 'Error: ' + data.error;
                document.getElementById('resultText').className = '';
                return;
            }
            updateUI(data.result, data.confidence);
        } catch(err) {
            document.getElementById('resultText').innerText = 'Connection error';
            document.getElementById('resultText').className = '';
        }
    };
    reader.readAsDataURL(file);
}
 
function updateUI(result, confidence) {
    document.getElementById('resultText').innerText = 'Detected: ' + result.toUpperCase();
    document.getElementById('resultText').className = '';
    document.getElementById('confidenceText').innerText = 'Confidence: ' + confidence + '%';
    document.getElementById('confFill').style.width = confidence + '%';
    ['bacteria','fungi','virus','others'].forEach(id => {
        document.getElementById(id).classList.remove('active');
        document.getElementById(id+'Text').innerText = 'No detection';
    });
    if (result === 'others') {
        activate('others');
        document.getElementById('othersText').innerText = 'Low confidence (' + confidence + '%)';
    } else {
        activate(result);
        document.getElementById(result+'Text').innerText = 'Detected (' + confidence + '%)';
    }
}
 
function activate(id) {
    document.getElementById(id).classList.add('active');
    document.getElementById(id+'Text').innerText = 'Detected ✅';
}
