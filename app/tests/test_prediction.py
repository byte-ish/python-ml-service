"""
Unit tests for prediction endpoint.
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_prediction() -> None:
    """
    Test the /predict endpoint with valid input.
    """
    response = client.post("/predict", json={"value": 2})
    assert response.status_code == 200
    assert "prediction" in response.json()