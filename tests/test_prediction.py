from unittest.mock import patch, MagicMock
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@patch("app.models.model_registry.ModelRegistry.is_registered")
@patch("app.models.model_registry.ModelRegistry.load_model")
@patch("app.models.model_registry.ModelRegistry.get_model_type")
def test_prediction_success(mock_get_model_type, mock_load_model, mock_is_registered):
    # Configure the mock for is_registered to always return True
    mock_is_registered.return_value = True

    # Configure the mock for get_model_type
    mock_get_model_type.return_value = "sklearn"

    # Configure the mock for load_model
    mock_model = MagicMock()
    mock_model.predict.return_value = ["Test input"]
    mock_load_model.return_value = mock_model

    payload = {"input": "Test input"}
    response = client.post("/predict/test_model", json=payload)

    # Debugging: Print the response JSON
    print("Response JSON:", response.json())

    assert response.status_code == 200
    assert response.json() == {"prediction": "Processed: Test input"}
