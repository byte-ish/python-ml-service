import pytest
from app.preprocessors.numerical_preprocessor import NumericalPreprocessor
from app.preprocessors.sklearn_preprocessor import SklearnPreprocessor


def test_numerical_preprocessor_success():
    preprocessor = NumericalPreprocessor()
    input_data = {"input": [[1.0, 2.0], [3.0, 4.0]]}
    result = preprocessor.preprocess(input_data)
    assert result == {"features": [[1.0, 2.0], [3.0, 4.0]]}


def test_numerical_preprocessor_invalid_input():
    preprocessor = NumericalPreprocessor()
    with pytest.raises(ValueError):
        preprocessor.preprocess({"input": "invalid"})


def test_sklearn_preprocessor_success():
    preprocessor = SklearnPreprocessor()
    input_data = {"input": "Test Input"}
    result = preprocessor.preprocess(input_data)
    assert result == {"features": ["test input"]}
