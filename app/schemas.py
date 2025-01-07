# app/schemas.py
from pydantic import BaseModel, Field

# Input schema for Model A
class ModelAInput(BaseModel):
    text: str = Field(
        ...,
        description="Input text for Model A.",
        example="This is a test input for Model A."
    )

# Input schema for Model B
class ModelBInput(BaseModel):
    numbers: list[float] = Field(
        ...,
        description="Input list of numbers for Model B.",
        example=[1.0, 2.5, 3.3]
    )

# Output schema for Model A
class ModelAOutput(BaseModel):
    sentiment: str = Field(
        ...,
        description="Sentiment analysis result from Model A.",
        example="Positive"
    )

# Output schema for Model B
class ModelBOutput(BaseModel):
    sum: float = Field(
        ...,
        description="Sum of input numbers calculated by Model B.",
        example=6.8
    )