"""
Service for handling predictions.
"""
from app.models.ml_model import load_model, predict_with_model
from app.logger import LOGGER

# Load the model at startup
MODEL = load_model()

def predict(input_data: dict) -> list:
    """
    Predict the output based on input data using the loaded model.

    Args:
        input_data (dict): Input data for prediction.

    Returns:
        list: Prediction results.
    """
    LOGGER.debug("Performing prediction with input: %s", input_data)
    return predict_with_model(MODEL, input_data)