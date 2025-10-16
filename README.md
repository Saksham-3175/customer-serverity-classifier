# Customer Complaint Severity Classification

## 🎯 Objective
Train a deep learning model to classify **customer complaint severity** into `low`, `medium`, or `high`.  
The model is then exposed through a **FastAPI** endpoint for integration with a dashboard or any frontend system.

---

## 🧠 Project Overview

### Pipeline
1. **Data Preprocessing** — Clean complaint narratives, remove noise, and normalize text.  
2. **Weak Supervision** — Generate pseudo-labels (`low`, `medium`, `high`) using TextBlob polarity and escalation keywords.  
3. **Deep Learning Model** — Train a Bidirectional LSTM classifier using TensorFlow/Keras.  
4. **Evaluation & Visualization** — Plot accuracy/loss, confusion matrix, class distribution, and word clouds.  
5. **Deployment** — Convert trained model into a **FastAPI** inference service.  
6. **Dashboard Integration** — Frontend consumes the API endpoint to visualize and prioritize complaints.

---

## 🧩 Repository Structure

```
customer-severity-classifier/
│
├── data/
│   ├── complaints_raw.csv
│   └── complaints_processed.csv
│
├── notebooks/
│   └── severity_classifier_tf_viz.ipynb
│
├── artifacts/
│   ├── severity_lstm_tf.keras
│   ├── severity_lstm_tf_tokenizer.pkl
│   └── severity_lstm_tf_labels.json
│
├── src/
│   ├── data_prep.py
│   ├── model_train.py
│   ├── evaluate.py
│   └── infer.py
│
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── utils.py
│
├── dashboard/
│   └── README.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Setup Instructions

### 1. Create environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

### 2. Train model
Open `notebooks/severity_classifier_tf_viz.ipynb` and run all cells.  
Artifacts (model, tokenizer, labels) will be saved in `artifacts/`.

### 3. Run API
```bash
uvicorn api.main:app --reload
```
Access the API docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

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

## 🧮 Model Details
- Architecture: **Bidirectional LSTM**
- Embedding Dim: `128`
- LSTM Units: `96`
- Dropout: `0.3`
- Loss: `SparseCategoricalCrossentropy`
- Optimizer: `Adam`
- Evaluation: Accuracy, F1-score, Confusion Matrix

---

## 📊 Visualizations
- Accuracy vs Validation Accuracy  
- Loss vs Validation Loss  
- Confusion Matrix Heatmap  
- Class Distribution Plot  
- WordClouds per severity level

---

## 🧠 API Structure

| Endpoint | Method | Description |
|-----------|---------|-------------|
| `/` | GET | Health check |
| `/predict` | POST | Predicts severity from complaint text |

---

## 👥 Team Workflow

| Role | Responsibility |
|------|----------------|
| **Model Team** | Train and optimize LSTM model |
| **API Team** | Serve model via FastAPI |
| **Dashboard Team** | Consume `/predict` endpoint and visualize results |

---

## ⚙️ Tech Stack
- Python 3.10+  
- TensorFlow / Keras  
- TextBlob  
- FastAPI  
- Matplotlib / Seaborn / WordCloud  

---

## 📁 Outputs
- `severity_lstm_tf.keras` — model weights  
- `severity_lstm_tf_tokenizer.pkl` — tokenizer object  
- `severity_lstm_tf_labels.json` — label mappings  
- `/predict` API endpoint for real-time inference

---

## 🧩 Future Improvements
- Move from LSTM → Transformer-based model (DistilBERT)  
- Add confidence calibration and explainability layer  
- Containerize API using Docker  
- Integrate continuous retraining pipeline (CI/CD)

---