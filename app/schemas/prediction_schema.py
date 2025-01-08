"""
Schemas for request and response validation for the prediction endpoint.
"""

from typing import Union, List
from pydantic import BaseModel, Field, root_validator  # Ensure Pydantic is installed


class PredictionInput(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Schema for input data required by the prediction endpoint.
    """
    input: Union[str, List[List[float]]] = Field(
        ...,
        description=(
            "Input data for the model. For text-based models, provide a string. "
            "For numerical models, provide a list of lists."
        ),
        example="I love this product",
    )

    @root_validator(pre=True)
    def validate_input(cls, values):  # pylint: disable=no-self-argument
        """
        Validate input field based on the input type
        (string for text models or list for numerical models).

        Args:
            values (dict): Input values to validate.

        Returns:
            dict: Validated input values.

        Raises:
            ValueError: If the input is invalid.
        """
        input_data = values.get("input")

        # Check for valid string input
        if isinstance(input_data, str):
            return values

        # Check for valid numerical input
        if (
            isinstance(input_data, list) and
            all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in input_data)
        ):
            return values

        raise ValueError(
            "'input' must be a string for text-based models or a list of numerical lists for numerical models."
        )


class PredictionResponse(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Schema for the prediction response data.
    """
    prediction: Union[str, List[float]] = Field(
        ...,
        description=(
            "The processed prediction result from the ML model. For text-based models, "
            "provide a string. For numerical models, provide a list of floats."
        ),
        example=(
            "Processed: positive sentiment for text models or "
            "[6.0, 15.0] for numerical models."
        ),
    )
