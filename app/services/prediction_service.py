from app.models.model_loader import load_model
from app.schemas import PredictionInput
from app.logger import get_logger
from app.exceptions import PredictionError

logger = get_logger(__name__)
model = load_model()

def predict(data: PredictionInput):
    """Perform prediction using the loaded model."""
    try:
        # Input should be a 2D list for the Iris model
        input_data = [data.features]
        prediction = model.predict(input_data)
        logger.info(f"Prediction successful: {prediction}")
        return prediction.tolist()
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise PredictionError("Error during prediction.")