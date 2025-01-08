
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
