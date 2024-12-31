"""
Generates and saves a sample mock model for testing.
"""

import pickle
from app.models.mock_string_model import MockStringModel
import logging

logger = logging.getLogger(__name__)

def generate_mock_model():
    """
    Generates and saves a mock model for testing string input/output.
    """
    logger.info("Generating mock model...")
    mock_model = MockStringModel()
    with open("app/models/model.pkl", "wb") as f:
        pickle.dump(mock_model, f)
    logger.info("Mock model saved successfully at 'app/models/model.pkl'")

if __name__ == "__main__":
    generate_mock_model()