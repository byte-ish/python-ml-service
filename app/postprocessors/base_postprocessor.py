"""
Base class for output postprocessing.
"""

# pylint: disable=too-few-public-methods
class BasePostprocessor:
    """
    Base class for output postprocessing.
    Defines the interface for all postprocessors.
    """

    def postprocess(self, prediction) -> str:
        """
        Postprocess the model output.

        Args:
            prediction: Raw model output.

        Returns:
            str: Postprocessed output.
        """
        raise NotImplementedError("Postprocessor must implement the 'postprocess' method.")
