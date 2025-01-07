class BasePostprocessor:
    """
    Base class for output postprocessing.
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