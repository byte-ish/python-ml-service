"""
Preprocessor for numerical models.
"""
from app.preprocessors.base_preprocessor import BasePreprocessor
from app.utils.logger import get_logger

logger = get_logger(__name__)


class NumericalPreprocessor(BasePreprocessor):
    def preprocess(self, input_data):
        try:
            features = input_data.get("input")
            if not isinstance(features, list) or not all(isinstance(row, list) for row in features):
                raise ValueError("For 'numerical', 'input' must be a list of numerical lists.")
            return {"features": features}
        except Exception as e:
            raise ValueError(f"Error during numerical preprocessing: {e}")