from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_health_check():
    """Kiểm tra xem API có sống không"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_sentiment_prediction():
    """Kiểm tra logic dự báo cảm xúc"""
    payload = {"text": "I love this AI course!"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "label" in response.json()
    assert response.json()["label"] in ["POSITIVE", "NEGATIVE"]