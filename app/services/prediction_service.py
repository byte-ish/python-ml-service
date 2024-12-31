"""
Business logic for making predictions using the ML model.
"""

from app.models.model_loader import load_model
from app.logger import get_logger
from app.exceptions import PredictionError

logger = get_logger(__name__)
model = load_model()


def predict(data, request_id):
    """
    Perform prediction using the loaded model.

    Args:
        data (PredictionInput): Validated input data.
        request_id (str): Unique ID for tracking the request.

    Returns:
        str: Prediction result from the model.
    """
    try:
        input_text = data.input_text
        logger.info(f"Processing input: {input_text}", extra={"request_id": request_id})

        # Perform prediction
        prediction = model.predict([input_text])[0]
        logger.info(f"Prediction successful: {prediction}", extra={"request_id": request_id})
        return prediction
    except ValueError as e:
        logger.error(f"Value error during prediction: {str(e)}", extra={"request_id": request_id})
        raise PredictionError("Invalid input for prediction.")
    except Exception as e:
        logger.error(f"Unexpected error during prediction: {str(e)}", extra={"request_id": request_id})
        raise