"""
Healthcheck route for the microservice.
"""
from fastapi import APIRouter
from app.logger import LOGGER

router = APIRouter()

@router.get("/healthcheck", tags=["Health"])
async def healthcheck() -> dict:
    """
    Endpoint to check the service's health.

    Returns:
        dict: Health status.
    """
    LOGGER.info("Healthcheck endpoint accessed.")
    return {"status": "healthy"}