import numpy as np
from app.postprocessors.base_postprocessor import BasePostprocessor
from app.logger import get_logger

logger = get_logger(__name__)

class NumericalPostprocessor(BasePostprocessor):
    """
    Postprocessor for numerical models.
    """

    def postprocess(self, raw_prediction) -> str:
        """
        Convert raw numerical output into a formatted string.

        Args:
            raw_prediction: Raw output from the numerical model.

        Returns:
            str: Postprocessed prediction result.
        """
        try:
            logger.info(f"Postprocessing raw prediction: {raw_prediction}")

            # Handle numpy array or other iterable formats
            if isinstance(raw_prediction, np.ndarray):
                raw_prediction = raw_prediction.tolist()

            if not isinstance(raw_prediction, (list, tuple)):
                raise ValueError("Raw prediction must be a list or tuple.")

            # Format the result as a string
            formatted_result = f"Processed numerical result: {raw_prediction}"
            logger.info(f"Formatted numerical result: {formatted_result}")

            return formatted_result
        except Exception as e:
            logger.error(f"Error during numerical postprocessing: {e}", exc_info=True)
            raise ValueError(f"Error during numerical postprocessing: {e}")