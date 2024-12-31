"""
Business logic for making predictions using the ML model.
"""

from app.models.model_loader import load_model
from app.logger import get_logger
from app.exceptions import PredictionError

logger = get_logger(__name__)
model = load_model()

def predict(data):
    """
    Perform prediction using the loaded model.

    Args:
        data (PredictionInput): Validated input data.

    Returns:
        str: Prediction result from the model.
    """
    try:
        input_text = data.input_text
        logger.info(f"Received input for prediction: {input_text}")

        # Perform prediction
        prediction = model.predict([input_text])[0]  # Assuming model returns a list
        logger.info(f"Prediction result: {prediction}")
        return prediction
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise PredictionError("Error during prediction.")