import os

TESTS = {
    "tests/test_main.py": """
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_startup():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Service is running"}
""",
    "tests/test_mock_string_model.py": """
import pytest
from app.models.mock_string_model import MockStringModel

def test_mock_model_fit():
    model = MockStringModel()
    assert model.fit(["input"]) == model

def test_mock_model_predict():
    model = MockStringModel()
    result = model.predict(["test input"])
    assert result == ["Processed: test input"]
""",
    "tests/test_model_registry.py": """
import pytest
from app.models.model_registry import ModelRegistry

def test_model_registry_register():
    ModelRegistry.register_model("test_model", "path/to/model", "test_type")
    assert ModelRegistry.is_registered("test_model")

def test_model_registry_load_model_not_found():
    with pytest.raises(KeyError):
        ModelRegistry.load_model("non_existent_model")
""",
    "tests/test_base_postprocessor.py": """
import pytest
from app.postprocessors.base_postprocessor import BasePostprocessor

def test_base_postprocessor_not_implemented():
    with pytest.raises(NotImplementedError):
        BasePostprocessor().postprocess(None)
""",
    "tests/test_sklearn_preprocessor.py": """
import pytest
from app.preprocessors.sklearn_preprocessor import SklearnPreprocessor

def test_sklearn_preprocessor_valid():
    preprocessor = SklearnPreprocessor()
    result = preprocessor.preprocess({"input": "Test Input"})
    assert result == {"features": ["test input"]}

def test_sklearn_preprocessor_invalid():
    preprocessor = SklearnPreprocessor()
    with pytest.raises(ValueError):
        preprocessor.preprocess({"input": 12345})
""",
    "tests/test_prediction_service.py": """
import pytest
from unittest.mock import MagicMock, patch
from app.services.prediction_service import predict

@patch("app.models.model_registry.ModelRegistry.load_model")
@patch("app.models.model_registry.ModelRegistry.get_model_type")
def test_prediction_flow(mock_get_model_type, mock_load_model):
    mock_get_model_type.return_value = "sklearn"
    mock_model = MagicMock()
    mock_model.predict.return_value = ["Processed output"]
    mock_load_model.return_value = mock_model

    result = predict({"input": "test input"}, "test_model", "request_id")
    assert result == "Processed output"
""",
    "tests/test_logger.py": """
from app.utils.logger import get_logger

def test_logger_initialization():
    logger = get_logger("test_logger")
    assert logger.name == "test_logger"
    assert logger.hasHandlers()
""",
}

def create_test_files():
    os.makedirs("tests", exist_ok=True)
    for filename, content in TESTS.items():
        with open(filename, "w") as f:
            f.write(content)
    print("Test files created successfully.")

if __name__ == "__main__":
    create_test_files()