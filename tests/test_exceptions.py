import pytest
from app.exceptions import PredictionError, ServiceError

def test_prediction_error():
    with pytest.raises(PredictionError) as excinfo:
        raise PredictionError("Test prediction error")
    assert excinfo.value.status_code == 400
    assert excinfo.value.detail == "Test prediction error"

def test_service_error():
    with pytest.raises(ServiceError) as excinfo:
        raise ServiceError("Test service error")
    assert excinfo.value.status_code == 500
    assert excinfo.value.detail == "Test service error"