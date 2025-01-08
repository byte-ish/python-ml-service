"""
Preprocessor for sklearn-based models.
"""

# pylint: disable=too-few-public-methods
from app.preprocessors.base_preprocessor import BasePreprocessor
from app.utils.logger import get_logger

logger = get_logger(__name__)


class SklearnPreprocessor(BasePreprocessor):
    """
    Preprocessor for sklearn-based models.
    """

    def preprocess(self, input_data):
        """
        Preprocess the input data for sklearn-based models.

        Args:
            input_data (dict): Input data containing 'input', which must be a string.

        Returns:
            dict: Processed data with extracted features.

        Raises:
            ValueError: If the input is invalid or processing fails.
        """
        try:
            text = input_data.get("input")
            if not isinstance(text, str):
                raise ValueError("For 'sklearn', 'input' must be a string.")
            preprocessed_text = text.lower()
            return {"features": [preprocessed_text]}
        except Exception as e:
            raise ValueError(f"Error during sklearn preprocessing: {e}") from e
