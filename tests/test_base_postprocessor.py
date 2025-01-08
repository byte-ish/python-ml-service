
import pytest
from app.postprocessors.base_postprocessor import BasePostprocessor

def test_base_postprocessor_not_implemented():
    with pytest.raises(NotImplementedError):
        BasePostprocessor().postprocess(None)
