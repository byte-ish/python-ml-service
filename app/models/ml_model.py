"""
Handles ML model loading and prediction.
"""
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import os
from app.logger import LOGGER

MODEL_PATH = os.getenv("MODEL_PATH", "model.pkl")

def train_mock_model() -> None:
    """
    Train and save a mock Logistic Regression model.
    """
    LOGGER.info("Training a new mock model.")
    x_data = np.array([[0], [1], [2], [3]])
    y_data = np.array([0, 0, 1, 1])
    model = LogisticRegression()
    model.fit(x_data, y_data)

    with open(MODEL_PATH, "wb") as file:
        pickle.dump(model, file)
    LOGGER.info("Mock model saved at %s", MODEL_PATH)

def load_model() -> LogisticRegression:
    """
    Load the pre-trained model or train a new one if unavailable.

    Returns:
        LogisticRegression: Loaded model instance.
    """
    try:
        with open(MODEL_PATH, "rb") as file:
            model = pickle.load(file)
        LOGGER.info("Model loaded successfully.")
        return model
    except FileNotFoundError:
        LOGGER.warning("Model not found. Training a new one.")
        train_mock_model()
        return load_model()

def predict_with_model(model: LogisticRegression, input_data: dict) -> list:
    """
    Make a prediction using the given model.

    Args:
        model (LogisticRegression): The loaded model.
        input_data (dict): Input data for prediction.

    Returns:
        list: Prediction results.
    """
    x_data = np.array([input_data["value"]]).reshape(-1, 1)
    return model.predict(x_data).tolist()