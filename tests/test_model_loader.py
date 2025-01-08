import pytest
from unittest.mock import patch
from app.models.model_loader import load_model
from app.models.model_registry import ModelRegistry

@patch("app.models.model_registry.ModelRegistry.load_model")
def test_load_model(mock_load_model):
    mock_load_model.return_value = "mock_model"
    model = load_model("test_model")
    assert model == "mock_model"

def test_load_model_not_registered():
    with pytest.raises(KeyError):
        load_model("unknown_model")
