"""
Postprocessor for numerical models.
"""

import numpy as np
from app.postprocessors.base_postprocessor import BasePostprocessor
from app.utils.logger import get_logger

logger = get_logger(__name__)


class NumericalPostprocessor(BasePostprocessor):  # pylint: disable=too-few-public-methods
    """
    Postprocessor for numerical models.
    """

    def postprocess(self, prediction) -> str:
        """
        Convert raw numerical output into a formatted string.

        Args:
            prediction: Raw output from the numerical model.

        Returns:
            str: Postprocessed prediction result.
        """
        try:
            logger.info("Postprocessing raw prediction: %s", prediction)

            if isinstance(prediction, np.ndarray):
                prediction = prediction.tolist()

            if not isinstance(prediction, (list, tuple)):
                raise ValueError("Raw prediction must be a list or tuple.")

            formatted_result = f"Processed numerical result: {prediction}"
            logger.info("Formatted numerical result: %s", formatted_result)

            return formatted_result
        except Exception as e:
            logger.error("Error during numerical postprocessing: %s", e, exc_info=True)
            raise ValueError(f"Error during numerical postprocessing: {e}") from e
