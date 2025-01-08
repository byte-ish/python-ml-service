from pydantic import ValidationError
from app.schemas.prediction_schema import PredictionInput, PredictionResponse

def test_prediction_input_valid_string():
    input_data = {"input": "Test input"}
    schema = PredictionInput(**input_data)
    assert schema.input == "Test input"

def test_prediction_input_invalid_data():
    input_data = {"input": 12345}
    try:
        PredictionInput(**input_data)
    except ValidationError as e:
        assert "'input' must be a string for text-based models or a list of numerical lists for numerical models." in str(e)

def test_prediction_response():
    response_data = {"prediction": "Test prediction"}
    schema = PredictionResponse(**response_data)
    assert schema.prediction == "Test prediction"
