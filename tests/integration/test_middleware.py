from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_request_id_middleware():
    response = client.get("/health")
    assert "X-Request-ID" in response.headers
    assert len(response.headers["X-Request-ID"]) > 0
