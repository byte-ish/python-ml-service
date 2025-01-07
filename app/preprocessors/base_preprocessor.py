class BasePreprocessor:
    """
    Base class for input preprocessing.
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