"""
Registry for preprocessors and postprocessors for different model types.
"""
from app.preprocessors.sklearn_preprocessor import SklearnPreprocessor
from app.postprocessors.sklearn_postprocessor import SklearnPostprocessor
from app.preprocessors.numerical_preprocessor import NumericalPreprocessor
from app.postprocessors.numerical_postprocessor import NumericalPostprocessor
from app.utils.logger import get_logger

logger = get_logger(__name__)


class ProcessorRegistry:
    """
    Registry to manage preprocessors and postprocessors for different model types.
    """

    _preprocessors = {
        "sklearn": SklearnPreprocessor,
        "numerical": NumericalPreprocessor,
    }

    _postprocessors = {
        "sklearn": SklearnPostprocessor,
        "numerical": NumericalPostprocessor,
    }

    @staticmethod
    def get_preprocessor(model_type: str):
        """
        Retrieve the preprocessor for the specified model type.
        """
        if model_type not in ProcessorRegistry._preprocessors:
            logger.error(f"Preprocessor not found for model type: {model_type}")
            raise ValueError(f"Preprocessor not found for model type: {model_type}")
        logger.info(f"Preprocessor found for model type: {model_type}")
        return ProcessorRegistry._preprocessors[model_type]()

    @staticmethod
    def get_postprocessor(model_type: str):
        """
        Retrieve the postprocessor for the specified model type.
        """
        if model_type not in ProcessorRegistry._postprocessors:
            logger.error(f"Postprocessor not found for model type: {model_type}")
            raise ValueError(f"Postprocessor not found for model type: {model_type}")
        logger.info(f"Postprocessor found for model type: {model_type}")
        return ProcessorRegistry._postprocessors[model_type]()