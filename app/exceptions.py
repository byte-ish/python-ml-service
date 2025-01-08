"""
Defines custom exceptions and standardized error responses for the microservice.
"""

from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_400_BAD_REQUEST


class PredictionError(HTTPException):
    """
    Custom exception for errors during the prediction process.
    """

    def __init__(self, detail: str = "Error occurred during prediction"):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)


class ServiceError(HTTPException):
    """
    Custom exception for unexpected service errors.
    """

    def __init__(self, detail: str = "Internal service error"):
        super().__init__(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
