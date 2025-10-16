import pytest
from fastapi.testclient import TestClient
from api.system import router as system_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(system_router)

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert "message" in json_data["data"]

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["status"] == "success"
    assert json_data["data"]["status"] == "OK"
