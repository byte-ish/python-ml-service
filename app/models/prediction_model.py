"""
Pydantic model for prediction input validation.
"""
from pydantic import BaseModel, Field


class PredictionInput(BaseModel):
    """
    Input schema for prediction requests.
    """
    value: float = Field(..., description="Input value for prediction")