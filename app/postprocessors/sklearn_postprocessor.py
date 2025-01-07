# app/postprocessors/sklearn_postprocessor.py
from app.postprocessors.base_postprocessor import BasePostprocessor


class SklearnPostprocessor(BasePostprocessor):
    """
    Postprocessor for sklearn models.
    """

    def postprocess(self, raw_prediction) -> str:
        """
        Convert raw model output into a human-readable format.

        Args:
            raw_prediction: Raw output from the model.

        Returns:
            str: Postprocessed prediction result.
        """
        return f"Processed: {raw_prediction[0]}"