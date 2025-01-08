
import pytest
from app.preprocessors.base_preprocessor import BasePreprocessor

def test_base_preprocessor():
    preprocessor = BasePreprocessor()
    with pytest.raises(NotImplementedError):
        preprocessor.preprocess({"input": "test"})
