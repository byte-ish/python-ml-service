"""
Loads the serialized ML model from a file.
"""

import pickle
from app.models.mock_string_model import MockStringModel  # Ensure import for unpickling
from app.config import Config
import logging

logger = logging.getLogger(__name__)

def load_model():
    """
    Load the ML model from the path specified in the configuration.

    Returns:
        object: The loaded ML model.
    """
    model_path = Config.MODEL_PATH
    try:
        logger.info(f"Loading model from {model_path}...")
        with open(model_path, "rb") as file:
            model = pickle.load(file)
        logger.info("Model loaded successfully.")
        return model
    except FileNotFoundError:
        logger.error(f"Model file not found at {model_path}.")
        raise
    except Exception as e:
        logger.error(f"Error while loading the model: {str(e)}")
        raise