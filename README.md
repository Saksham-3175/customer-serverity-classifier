# Customer Complaint Severity Classification

## Overview

This project provides a deep learning-based solution to classify customer complaints into three severity levels: `low`, `medium`, or `high`.  
The trained model is served via a **FastAPI** backend with an integrated frontend for visualization and testing.

The system is designed for seamless deployment, either locally, via Docker, or directly on cloud platforms like Render.

---

## Features

- **Deep Learning Model** – Bidirectional LSTM classifier for complaint severity.
- **Integrated API & Frontend** – No separate frontend server required.
- **Dockerized Deployment** – Pre-built Docker image or custom build.
- **FastAPI Documentation** – Swagger UI available at `/docs`.

---

## Installation & Local Run

Clone the repository:

```bash
git clone https://github.com/Saksham-3175/customer-serverity-classifier.git
cd customer-serverity-classifier
```

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

Run the application:

```bash
python app.py
```

Access:

- **Frontend:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **API Docs:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Deployment Options

1. **Render (Automatic Deployment)**

   Deploy directly using the repository via Render:

   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Saksham-3175/customer-serverity-classifier)

2. **Docker**

   - **Pre-built image:**

     ```bash
     docker run -p 8000:8000 virajsh/customer-serverity-classifier:latest
     ```

   - **Build from Dockerfile:**

     ```bash
     docker build -t customer-severity-classifier .
     docker run -p 8000:8000 customer-severity-classifier
     ```

3. **Local Run**

   Simply run `python app.py` after installing dependencies (development environment).

---

## Model Details

- **Architecture:** Bidirectional LSTM
- **Embedding Dimension:** 128
- **LSTM Units:** 96
- **Dropout:** 0.3
- **Loss:** SparseCategoricalCrossentropy
- **Optimizer:** Adam
- **Evaluation Metrics:** Accuracy, F1-score, Confusion Matrix

The model uses weak supervision with sentiment polarity and escalation keywords to generate pseudo-labels for `low`, `medium`, and `high` severity levels.

---

## License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for full team details and roles.

---

## Notes

- API endpoints are automatically documented by FastAPI at `/docs`.
- Frontend and backend run under the same application – no separate server is required.
- Docker image is available publicly on Docker Hub: [`virajsh/customer-serverity-classifier:latest`](https://hub.docker.com/r/virajsh/customer-serverity-classifier/tags).
