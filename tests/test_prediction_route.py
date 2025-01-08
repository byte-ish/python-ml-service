from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@patch("app.models.model_registry.ModelRegistry.is_registered", return_value=True)
@patch("app.models.model_registry.ModelRegistry.get_model_type", return_value="sklearn")
@patch("app.models.model_registry.ModelRegistry.load_model")
@patch("app.services.prediction_service.ProcessorRegistry.get_preprocessor")
@patch("app.services.prediction_service.ProcessorRegistry.get_postprocessor")
def test_prediction_endpoint(
    mock_postprocessor, mock_preprocessor, mock_load_model, *_mocks
):
    mock_model = MagicMock()
    mock_model.predict.return_value = ["Processed: Test Input"]
    mock_load_model.return_value = mock_model

    preprocessor = MagicMock()
    preprocessor.preprocess.return_value = {"features": ["test input"]}
    mock_preprocessor.return_value = preprocessor

    postprocessor = MagicMock()
    postprocessor.postprocess.return_value = "Processed Result"
    mock_postprocessor.return_value = postprocessor

    response = client.post("/predict/test_model", json={"input": "Test Input"})
    assert response.status_code == 200
    assert response.json() == {"prediction": "Processed Result"}
