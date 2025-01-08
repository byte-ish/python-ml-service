"""
Common schemas for shared data structures.
"""
from pydantic import BaseModel, Field


class HealthCheckResponse(BaseModel):
    """
    Schema for the health check response.
    """
    status: str = Field(
        ...,
        description="Health status of the service.",
        example="Healthy",
    )
    version: str = Field(
        ...,
        description="Version of the service.",
        example="1.0",
    )
