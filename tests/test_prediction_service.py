from app.services.prediction_service import predict
from app.schemas import PredictionInput

def test_prediction_logic():
    sample_input = PredictionInput(features=[1.2, 3.4, 5.6, 7.8])
    result = predict(sample_input)
    assert isinstance(result, list)
    assert len(result) == 1  # Assuming the model outputs a single prediction