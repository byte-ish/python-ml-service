"""
Defines the MockStringModel used as a placeholder for testing string input/output.
"""
import logging
from sklearn.base import BaseEstimator, TransformerMixin

logger = logging.getLogger(__name__)


class MockStringModel(BaseEstimator, TransformerMixin):  # pylint: disable=too-few-public-methods
    """
    Mock model for string input and output.
    """

    def fit(self, x, y=None):  # pylint: disable=invalid-name,unused-argument
        """
        Fit the model (mock implementation).

        Args:
            x: Input data.
            y: Target data (optional).

        Returns:
            MockStringModel: self
        """
        logger.info("MockStringModel: fit method called with data")
        return self

    def predict(self, x):  # pylint: disable=invalid-name
        """
        Predict using the model (mock implementation).

        Args:
            x: Input data.

        Returns:
            list: Mock predictions.
        """
        logger.info("MockStringModel: predict method called")
        predictions = [f"Processed: {text}" for text in x]
        logger.info("MockStringModel: Predictions generated - %s", predictions)
        return predictions
