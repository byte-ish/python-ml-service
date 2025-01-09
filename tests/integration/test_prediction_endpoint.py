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
