"""
Unit tests for healthcheck endpoint.
"""
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_healthcheck() -> None:
    """
    Test the /healthcheck endpoint.
    """
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}