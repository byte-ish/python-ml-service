from app.postprocessors.base_postprocessor import BasePostprocessor

class SklearnPostprocessor(BasePostprocessor):
    def postprocess(self, raw_prediction) -> str:
        return f"Processed: {raw_prediction[0]}"