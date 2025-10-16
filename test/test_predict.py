import pytest
from fastapi.testclient import TestClient
from api.predict import router as predict_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(predict_router)

client = TestClient(app)

def test_predict_single_text():
    response = client.post("/predict", json={"texts": "They stole my money and refuse to refund."})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert "predictions" in json_data["data"]
    assert len(json_data["data"]["predictions"]) == 1
    prediction = json_data["data"]["predictions"][0]
    assert "severity" in prediction
    assert "confidence" in prediction
    assert "prediction_time_ms" in prediction

def test_predict_batch_texts():
    texts = [
        "They stole my money and refuse to refund.",
        "The product was defective and not delivered on time."
    ]
    response = client.post("/predict", json={"texts": texts})
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert len(json_data["data"]["predictions"]) == 2

def test_predict_invalid_input():
    response = client.post("/predict", json={"texts": 12345})
    assert response.status_code == 422

