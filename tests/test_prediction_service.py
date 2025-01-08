import pytest
from unittest.mock import MagicMock, patch
from app.services.prediction_service import predict

@patch("app.models.model_registry.ModelRegistry.load_model")
@patch("app.models.model_registry.ModelRegistry.get_model_type")
@patch("app.config.registry.ProcessorRegistry.get_postprocessor")
@patch("app.config.registry.ProcessorRegistry.get_preprocessor")
def test_prediction_flow(mock_get_preprocessor, mock_get_postprocessor, mock_get_model_type, mock_load_model):
    # Mocking the model type
    mock_get_model_type.return_value = "sklearn"

    # Mocking the model
    mock_model = MagicMock()
    mock_model.predict.return_value = ["Processed output"]
    mock_load_model.return_value = mock_model

    # Mocking the preprocessor
    mock_preprocessor = MagicMock()
    mock_preprocessor.preprocess.return_value = {"features": ["test input"]}
    mock_get_preprocessor.return_value = mock_preprocessor

    # Mocking the postprocessor
    mock_postprocessor = MagicMock()
    mock_postprocessor.postprocess.return_value = "Processed: Processed output"
    mock_get_postprocessor.return_value = mock_postprocessor

    # Performing the prediction
    result = predict({"input": "test input"}, "test_model", "request_id")

    # Asserting the final result matches the postprocessed result
    assert result == "Processed: Processed output"