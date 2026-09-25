from fastapi.testclient import TestClient
from app.api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_metrics():
    payload = {"cpu_percent": 10}
    response = client.post("/metrics", json=payload)
    assert response.status_code == 200
    assert client.get("/metrics/latest").json() == payload
