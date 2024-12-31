from fastapi import Request
from app.models.model_loader import load_model
from app.logger import get_logger

logger = get_logger(__name__)
model = load_model()

def predict(features, request: Request):
    """Make predictions and log with request ID."""
    try:
        prediction = model.predict([features])
        logger.info(
            f"Prediction successful: {prediction}",
            extra={"request_id": request.state.request_id}
        )
        return prediction.tolist()
    except Exception as e:
        logger.error(f"Prediction failed: {e}", extra={"request_id": request.state.request_id})
        raise