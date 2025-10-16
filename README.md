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
python -m http.server 5500
```

> **Note:** If you change the frontend port, update it in `./app.py` accordingly.

### 4. Example API request

**POST** `/predict`

```json
{
  "text": "My account was closed without prior notice."
}
```

**Response**

```json
{
  "severity": "high",
  "confidence": 0.92
}
```

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
