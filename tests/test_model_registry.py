
import pytest
from app.models.model_registry import ModelRegistry

def test_model_registry_register():
    ModelRegistry.register_model("test_model", "path/to/model", "test_type")
    assert ModelRegistry.is_registered("test_model")

def test_model_registry_load_model_not_found():
    with pytest.raises(KeyError):
        ModelRegistry.load_model("non_existent_model")
