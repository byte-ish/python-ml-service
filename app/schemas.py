from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    """
    Schema for input data required by the prediction endpoint.
    """
    features: list[float] = Field(
        ...,
        description="A list of numerical features to be used for prediction.",
        example=[5.1, 3.5, 1.4, 0.2],
    )