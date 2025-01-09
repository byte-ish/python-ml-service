from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@patch("app.routes.auth.requests.get")
def test_authentication_success(mock_jira_request):
    mock_jira_request.return_value.status_code = 200

    response = client.post(
        "/auth/jira-login",
        json={"email": "user@example.com", "api_token": "mock_api_token"}
    )
    assert response.status_code == 200
    actual_token = response.json()["access_token"]
    assert actual_token.startswith("eyJ")  # JWT tokens typically start with this
    assert len(actual_token.split(".")) == 3  # Ensure it follows JWT structure
