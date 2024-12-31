from pydantic import BaseModel
from typing import List

class PredictionInput(BaseModel):
    """Schema for input validation."""
    features: List[float]