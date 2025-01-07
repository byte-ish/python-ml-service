# app/config/registry.py
from app.preprocessors.sklearn_preprocessor import SklearnPreprocessor
from app.postprocessors.sklearn_postprocessor import SklearnPostprocessor


class ProcessorRegistry:
    """
    Registry to manage preprocessors and postprocessors for different model types.
    """

    _preprocessors = {
        "sklearn_model_a": SklearnPreprocessor,  # Corrected registration
        "sklearn_model_b": SklearnPreprocessor,  # Corrected registration
    }

    _postprocessors = {
        "sklearn_model_a": SklearnPostprocessor,  # Corrected registration
        "sklearn_model_b": SklearnPostprocessor,  # Corrected registration
    }

    @staticmethod
    def get_preprocessor(model_type: str):
        """
        Get the preprocessor for a specific model type.

        Args:
            model_type (str): The type of the model (e.g., 'sklearn_model_a').

        Returns:
            An instance of the preprocessor class.
        """
        if model_type not in ProcessorRegistry._preprocessors:
            raise ValueError(f"Preprocessor not found for model type: {model_type}")
        return ProcessorRegistry._preprocessors[model_type]()  # Instantiate without arguments

    @staticmethod
    def get_postprocessor(model_type: str):
        """
        Get the postprocessor for a specific model type.

        Args:
            model_type (str): The type of the model (e.g., 'sklearn_model_a').

        Returns:
            An instance of the postprocessor class.
        """
        if model_type not in ProcessorRegistry._postprocessors:
            raise ValueError(f"Postprocessor not found for model type: {model_type}")
        return ProcessorRegistry._postprocessors[model_type]()  # Instantiate without arguments