# Customer Complaint Severity Classification

## Objective

Train a deep learning model to classify customer complaint severity into `low`, `medium`, or `high`.
The trained model is exposed through a FastAPI service for integration with frontend or dashboard systems.

---

## Project Overview

### Pipeline

1. **Data Preprocessing** – Clean complaint text, remove noise, and normalize text.
2. **Weak Supervision** – Generate pseudo-labels (`low`, `medium`, `high`) using sentiment polarity and escalation keywords.
3. **Model Training** – Train a Bidirectional LSTM classifier using TensorFlow/Keras.
4. **Evaluation** – Assess model performance using accuracy, F1-score, and confusion matrix.
5. **Deployment** – Serve the trained model via FastAPI.
6. **Frontend Integration** – The development frontend consumes the API endpoint for severity visualization.

---

## Setup Instructions

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Saksham-3175/customer-serverity-classifier)

### 1. Environment Setup

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For development setup:

```bash
pip install -r requirements-dev.txt
```

---

### 2. Run the API

Start the FastAPI server:

```bash
python -m uvicorn app:app --reload
```

Access API documentation at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 3. Run the Frontend

Use a simple Python web server to serve the frontend:

```bash
python -m http.server 5500 --directory frontend
```

> **Note:** If you change the frontend port, update it in `./app.py` accordingly.

### 4. Example API request

### **POST** `/predict`

#### **Request Body (Single Complaint)**

```json
{
  "texts": ["My account was closed without prior notice."]
}
```

#### **Request Body (Multiple Complaints)**

```json
{
  "texts": [
    "My account was closed without prior notice.",
    "The product arrived damaged and customer support did not respond."
  ]
}
```

#### **Response (Single or Multiple)**

```json
{
  "status": "success",
  "data": {
    "predictions": [
      {
        "severity": "high",
        "confidence": 92.0,
        "prediction_time_ms": 231.4,
        "error": null
      },
      {
        "severity": "medium",
        "confidence": 85.5,
        "prediction_time_ms": 245.7,
        "error": null
      }
    ]
  },
  "errors": []
}
```

**Notes:**

- `texts` must be an array, even for a single complaint.
- Each element in `predictions` corresponds **line-by-line** to the `texts` array.
- `severity` is one of `"low"`, `"medium"`, `"high"`.
- `confidence` is in percentage (0–100).
- `prediction_time_ms` indicates inference time per request in milliseconds.

---

## Model Details

- Architecture: **Bidirectional LSTM**
- Embedding Dim: `128`
- LSTM Units: `96`
- Dropout: `0.3`
- Loss: `SparseCategoricalCrossentropy`
- Optimizer: `Adam`
- Evaluation: Accuracy, F1-score, Confusion Matrix

---
