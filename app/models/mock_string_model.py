"""
Defines the MockStringModel used as a placeholder for testing string input/output.
"""

from sklearn.base import BaseEstimator, TransformerMixin
import logging

logger = logging.getLogger(__name__)

class MockStringModel(BaseEstimator, TransformerMixin):
    """
    Mock model for string input and output.
    """

    def fit(self, X, y=None):
        logger.info("MockStringModel: fit method called with data")
        return self

    def predict(self, X):
        logger.info("MockStringModel: predict method called")
        predictions = [f"Processed: {text}" for text in X]
        logger.info(f"MockStringModel: Predictions generated - {predictions}")
        return predictions