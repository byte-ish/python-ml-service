from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    """
    Schema for input data required by the prediction endpoint.
    """
    input_text: str = Field(
        ...,
        description="A string input for the ML model to process and make predictions.",
        example="This is a sample input for the model.",
    )