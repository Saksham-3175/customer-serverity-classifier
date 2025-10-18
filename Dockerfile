FROM python:3.11-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY api ./api
COPY core ./core
COPY frontend ./frontend
COPY model ./model
COPY schema ./schema
COPY app.py .
COPY README.md .

RUN rm -rf model/dataset model/severity_classifier_tf_viz.ipynb test requirements-dev.txt render.yaml || true

EXPOSE 8000

CMD ["python", "app.py"]
