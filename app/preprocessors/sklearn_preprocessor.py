# app/preprocessors/sklearn_preprocessor.py
from app.preprocessors.base_preprocessor import BasePreprocessor
from app.logger import get_logger

logger = get_logger(__name__)

class SklearnPreprocessor(BasePreprocessor):
    """
    Preprocessor for sklearn models.
    """

    def preprocess(self, input_data):
        """
        Preprocess input data for sklearn models.

        Args:
            input_data (dict): Input data for preprocessing.

        Returns:
            dict: Preprocessed data with features ready for inference.
        """
        try:
            logger.info(f"Preprocessing input data: {input_data}")

            # Ensure input_data is a dictionary with the expected "text" field
            if not isinstance(input_data, dict):
                raise ValueError("Input data must be a dictionary.")

            text = input_data.get("text")
            if not isinstance(text, str):
                raise ValueError("The 'text' field must be a string.")

            # Perform preprocessing (e.g., converting to lowercase)
            preprocessed_text = text.lower()  # Example transformation
            logger.info(f"Preprocessed text: {preprocessed_text}")

            # Return features as required by the model
            return {"features": [preprocessed_text]}  # Ensure it's a list for compatibility

        except Exception as e:
            logger.error(f"Error during preprocessing: {str(e)}", exc_info=True)
            raise