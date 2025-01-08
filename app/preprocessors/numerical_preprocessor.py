"""
Preprocessor for numerical models.
"""
# pylint: disable=too-few-public-methods
from app.preprocessors.base_preprocessor import BasePreprocessor
from app.utils.logger import get_logger

logger = get_logger(__name__)


class NumericalPreprocessor(BasePreprocessor):
    """
    A preprocessor for numerical models. Validates and processes input data for numerical models.
    """

    def preprocess(self, input_data):
        """
        Preprocess the input data for numerical models.

        Args:
            input_data (dict): The input data containing 'input', which
            must be a list of numerical lists.

        Returns:
            dict: Processed data with extracted features.

        Raises:
            ValueError: If the input is invalid or processing fails.
        """
        try:
            features = input_data.get("input")
            if not isinstance(features, list) or not all(isinstance(row, list) for row in features):
                raise ValueError(
                    "For 'numerical', 'input' must be a list of numerical lists."
                )
            return {"features": features}
        except Exception as e:
            # Explicitly re-raising the exception with additional context
            raise ValueError(f"Error during numerical preprocessing: {e}") from e
