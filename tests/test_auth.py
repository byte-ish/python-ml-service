import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_jira_login_success(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 200
        return MockResponse()
    monkeypatch.setattr("requests.get", mock_get)

    payload = {"email": "test@example.com", "api_token": "valid_token"}
    response = client.post("/auth/jira-login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_jira_login_failure(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            status_code = 401
        return MockResponse()
    monkeypatch.setattr("requests.get", mock_get)

    payload = {"email": "test@example.com", "api_token": "invalid_token"}
    response = client.post("/auth/jira-login", json=payload)
    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid Jira credentials."}