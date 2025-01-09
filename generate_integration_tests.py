import os


def generate_integration_tests(base_dir="tests/integration"):
    """
    Generates integration tests for the project.
    """
    os.makedirs(base_dir, exist_ok=True)

    # Test Authentication Endpoint
    auth_test_content = """\
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
"""

    # Test JWT Utils
    jwt_utils_test_content = """\
from app.utils.jwt import verify_jwt_token

def test_jwt_invalid_token():
    invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyQGV4YW1wbGUuY29tIn0.invalidsignature"
    try:
        verify_jwt_token(invalid_token)
        assert False  # Should not reach here
    except Exception as e:
        assert "Signature verification failed" in str(e)
"""

    # Test Prediction Endpoint
    prediction_test_content = """\
from unittest.mock import patch, Mock
from fastapi.testclient import TestClient
from app.main import app
from app.models.mock_string_model import MockStringModel

client = TestClient(app)

@patch("app.models.model_registry.ModelRegistry.is_registered")
@patch("app.models.model_registry.ModelRegistry.load_model")
@patch("app.models.model_registry.ModelRegistry.get_model_type")
@patch("app.services.prediction_service.ProcessorRegistry.get_preprocessor")
@patch("app.services.prediction_service.ProcessorRegistry.get_postprocessor")
def test_prediction_success(mock_get_postprocessor, mock_get_preprocessor, mock_get_model_type, mock_load_model, mock_is_registered):
    mock_is_registered.return_value = True
    mock_load_model.return_value = MockStringModel()
    mock_get_model_type.return_value = "sklearn"

    mock_preprocessor = Mock()
    mock_preprocessor.preprocess.return_value = {"features": ["processed input"]}
    mock_get_preprocessor.return_value = mock_preprocessor

    mock_postprocessor = Mock()
    mock_postprocessor.postprocess.return_value = "Processed output"
    mock_get_postprocessor.return_value = mock_postprocessor

    response = client.post("/predict/test_model", json={"input": "Test input"})
    assert response.status_code == 200
    assert response.json()["prediction"] == "Processed output"

def test_prediction_invalid_input():
    response = client.post("/predict/test_model", json={"input": 123})
    assert response.status_code == 422
    assert "value_error" in response.json()["detail"][0]["type"]
"""

    # Write test files
    test_files = {
        "test_authentication_endpoint.py": auth_test_content,
        "test_jwt_utils.py": jwt_utils_test_content,
        "test_prediction_endpoint.py": prediction_test_content,
    }

    for filename, content in test_files.items():
        file_path = os.path.join(base_dir, filename)
        with open(file_path, "w") as f:
            f.write(content)

    print(f"Integration tests generated successfully in {base_dir}.")


if __name__ == "__main__":
    generate_integration_tests()