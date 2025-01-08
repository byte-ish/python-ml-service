"""
Postprocessor for sklearn-based models.
"""

# pylint: disable=too-few-public-methods
from app.postprocessors.base_postprocessor import BasePostprocessor

class SklearnPostprocessor(BasePostprocessor):
    """
    Postprocessor for sklearn-based models.
    """

    def postprocess(self, prediction) -> str:
        """
        Processes the raw prediction from the sklearn model.

        Args:
            prediction (list): Raw output from the sklearn model.

        Returns:
            str: Postprocessed prediction.
        """
        return f"Processed: {prediction[0]}"
