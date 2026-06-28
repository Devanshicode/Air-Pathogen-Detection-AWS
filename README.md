# 🧪 Air Pathogen Detection System
### AI-Powered Morphological Analysis | Deployed on AWS Serverless

![Status](https://img.shields.io/badge/Status-Live-brightgreen)
&nbsp;&nbsp;
![AWS](https://img.shields.io/badge/Cloud-AWS-orange)
&nbsp;&nbsp;
![Python](https://img.shields.io/badge/Python-3.11-blue)
&nbsp;&nbsp;
![ML](https://img.shields.io/badge/ML-CNN%20%7C%20ONNX-purple)
&nbsp;&nbsp;
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🌐 Live Demo
> **[Click here to open the live detection system](http://air-pathogen-frontend-devanshi.s3-website-us-east-1.amazonaws.com)**

Upload any microscopy image → get instant AI classification

---

## 📌 What This Project Does

This system detects airborne pathogens from microscopy images using a trained Convolutional Neural Network (CNN). It classifies images into 3 categories:

| Pathogen | Description |
|----------|-------------|
| 🦠 Bacteria | Bacterial morphological patterns |
| 🍄 Fungi | Fungal spore and hyphal structures |
| 🧬 Virus | Viral particle indicators |
| ⚪ Others | Low confidence / unclassified |

---

## 🏗️ Architecture
```

User uploads image
        ↓
S3 Static Website (Frontend)
        ↓
API Gateway (REST API - POST /predict)
        ↓
AWS Lambda (Python 3.11 - 512MB)
        ↓
S3 Model Bucket (model.onnx download)
        ↓
ONNX Runtime Inference
        ↓
DynamoDB (log prediction)
        ↓
JSON Response → UI Updates

```

---

## 🛠️ Tech Stack

### Machine Learning
| Component | Technology |
|-----------|------------|
| Model Architecture | Sequential CNN (Keras) |
| Training Framework | TensorFlow / Keras |
| Inference Format | ONNX Runtime |
| Input Shape | 224 × 224 × 3 (RGB) |
| Output Classes | 3 (Bacteria, Fungi, Virus) |
| Model Accuracy | ~72-75% |
| Training Platform | Google Colab |

### AWS Services
| Service | Purpose |
|---------|---------|
| AWS Lambda | Serverless inference engine |
| Amazon S3 | Model storage + frontend hosting |
| API Gateway | REST API endpoint |
| DynamoDB | Prediction logging |
| CloudWatch | Monitoring and logging |
| IAM | Security and permissions |

### Frontend
| Component | Technology |
|-----------|------------|
| UI | HTML5 + CSS3 + JavaScript |
| Design | Dark theme with animated detection strips |
| Hosting | S3 Static Website |

---

## 📸 Screenshots

### 🌐 Live Detection Working
![Detection Working](screenshots/22_website_detection_working.png)

### ☁️ S3 Model Bucket
![S3 Bucket](screenshots/02_s3_model_bucket.png)

### ⚡ Lambda Function
![Lambda Function](screenshots/07_lambda_function_created.png)

### 🔗 API Gateway
![API Gateway](screenshots/12_api_gateway.png)

### 🗄️ DynamoDB Predictions Logged
![DynamoDB](screenshots/23_dynamodb_prediction_logged.png)

---

## 🚀 How to Use

1. Open the **[Live Demo](http://air-pathogen-frontend-devanshi.s3-website-us-east-1.amazonaws.com)** link
2. Click **Choose File** and upload a microscopy image
3. Click **Detect Pathogen**
4. Wait 5-10 seconds for AI analysis
5. See result: Bacteria / Fungi / Virus + confidence %
6. Detection strip glows with color-coded result

---

## 📁 Repository Structure

air-pathogen-detection-aws/

├── README.md

├── lambda/

│   └── lambda_function.py    # AWS Lambda inference code

├── frontend/

│   ├── index.html            # Main UI

│   ├── style.css             # Dark theme styling

│   └── script.js             # API calls and UI updates

└── screenshots/              # AWS deployment screenshots


---

## ⚙️ AWS Deployment Summary

| Component | Details |
|-----------|---------|
| Lambda Memory | 512 MB |
| Lambda Timeout | 30 seconds |
| Lambda Runtime | Python 3.11 |
| Model Format | ONNX (converted from Keras .h5) |
| API Type | REST API - Regional |
| S3 Region | us-east-1 (N. Virginia) |
| Monthly Cost | $0 (AWS Free Tier) |

---

## 🧠 Key Technical Decisions

**Why ONNX instead of TFLite?**
TFLite runtime requires GLIBC 2.27+ which is unavailable on Lambda's Linux environment. ONNX Runtime has pre-built many linux wheels compatible with Lambda.

**Why Serverless (Lambda)?**
No server running 24/7. Lambda runs only when an image is submitted. Zero idle cost. Scales automatically with requests.

**Why S3 for model storage?**
Lambda has 250MB layer limit. Storing model in S3 and downloading to /tmp at runtime allows larger models and easy updates.

---

---


## 🎓 What This Project Taught Me

### ☁️ Cloud & AWS
- How to build a **fully serverless architecture** with zero idle cost
- How AWS services connect — S3 → Lambda → API Gateway → DynamoDB
- How IAM roles and least-privilege permissions work in real projects
- How to debug Lambda errors using **CloudWatch logs**
- How **Lambda layers** work and why size limits matter
- How to host a static website on S3 with public bucket policies
- How **API Gateway CORS** works and why it is needed for browser requests

### 🤖 Machine Learning & Deployment
- How to convert a Keras model from **.h5 → ONNX format** for deployment
- Why **TFLite had GLIBC compatibility issues** on Lambda and how I solved it
- How **ONNX Runtime** works as a Lambda-compatible inference engine
- How to preprocess images (resize → normalize → numpy array) for CNN inference
- How to cache ML models in Lambda using global variables to reduce latency

### 🐛 Problem Solving
- Debugged **GLIBC_2.27 not found** error — learned about Linux library compatibility
- Fixed **numpy binary incompatibility** between Python 3.11 and 3.13 builds
- Solved **CORS errors** by properly configuring API Gateway and redeploying
- Fixed **S3 bucket region mismatch** between CloudShell and bucket location
- Learned that **file extensions matter** — .html.txt vs .html breaks everything

### 💡 Key Realizations
- A working deployed project at 75% accuracy beats a perfect model sitting in Colab
- Serverless is not just cost-saving — it is **event-driven architecture thinking**
- Every error message is a learning opportunity — CloudWatch logs tell the whole story
- Cloud deployment has many moving parts — region, permissions, file formats, size limits all matter

---


## 👩‍💻 About

**Devanshi Barbhaya**
B.Tech CSE (Cloud Computing) | Silver Oak University, Ahmedabad
🔗 [LinkedIn](https://linkedin.com/in/devanshibarbhaya-5b62a0297)

---

## 📄 License
MIT License — feel free to use and modify
