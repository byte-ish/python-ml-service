import pytest
import numpy as np
from app.postprocessors.numerical_postprocessor import NumericalPostprocessor

def test_numerical_postprocessor_success():
    postprocessor = NumericalPostprocessor()
    prediction = np.array([1.0, 2.0, 3.0])
    result = postprocessor.postprocess(prediction)
    assert result == "Processed numerical result: [1.0, 2.0, 3.0]"

def test_numerical_postprocessor_invalid_input():
    postprocessor = NumericalPostprocessor()
    with pytest.raises(ValueError):
        postprocessor.postprocess("invalid")
