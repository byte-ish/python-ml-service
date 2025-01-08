"""
Schemas for request and response validation for the prediction endpoint.
"""
from typing import Union, List
from pydantic import BaseModel, Field, root_validator


class PredictionInput(BaseModel):
    """
    Schema for input data required by the prediction endpoint.
    """
    input: Union[str, List[List[float]]] = Field(
        ...,
        description="Input data for the model. For text-based models, provide a string. For numerical models, provide a list of lists.",
        example="I love this product",
    )

    @root_validator
    def validate_input(cls, values):
        """
        Validate input field based on the input type (string for text models or list for numerical models).
        """
        input_data = values.get("input")

        # Check for valid string input
        if isinstance(input_data, str):
            return values

        # Check for valid numerical input
        if isinstance(input_data, list) and all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in input_data):
            return values

        raise ValueError(
            "'input' must be a string for text-based models or a list of numerical lists for numerical models."
        )


class PredictionResponse(BaseModel):
    """
    Schema for the prediction response data.
    """
    prediction: Union[str, List[float]] = Field(
        ...,
        description="The processed prediction result from the ML model.",
        example="Processed: positive sentiment for text models or [6.0, 15.0] for numerical models.",
    )