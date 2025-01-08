"""
Preprocessor for sklearn-based models.
"""
from app.preprocessors.base_preprocessor import BasePreprocessor
from app.logger import get_logger

logger = get_logger(__name__)


class SklearnPreprocessor(BasePreprocessor):
    def preprocess(self, input_data):
        try:
            text = input_data.get("input")
            if not isinstance(text, str):
                raise ValueError("For 'sklearn', 'input' must be a string.")
            preprocessed_text = text.lower()
            return {"features": [preprocessed_text]}
        except Exception as e:
            raise ValueError(f"Error during sklearn preprocessing: {e}")