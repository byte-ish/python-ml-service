import pickle
from app.logger import get_logger
from app.config import Config
from app.exceptions import ModelNotFoundError

logger = get_logger(__name__)

def load_model():
    """Load the serialized ML model."""
    try:
        with open(Config.MODEL_PATH, "rb") as file:
            model = pickle.load(file)
            logger.info("Model loaded successfully.")
            return model
    except FileNotFoundError:
        logger.error(f"Model file not found at {Config.MODEL_PATH}.")
        raise ModelNotFoundError("Model file not found.")
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        raise