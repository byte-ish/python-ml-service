"""
Base class for input preprocessing.
"""

# pylint: disable=too-few-public-methods
class BasePreprocessor:
    """
    Base class for input preprocessing.
    Defines the interface for all preprocessors.
    """

    def preprocess(self, input_data: dict) -> dict:
        """
        Preprocess the input data.

        Args:
            input_data (dict): Raw input data.

        Returns:
            dict: Preprocessed input data.
        """
        raise NotImplementedError("Preprocessor must implement the 'preprocess' method.")
