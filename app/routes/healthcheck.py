from fastapi import APIRouter, Request
from app.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.get(
    "/health",
    tags=["Health"],
    summary="Health Check Endpoint",
    description="Returns the health status of the microservice to confirm it is running and operational.",
    responses={
        200: {
            "description": "Successful response indicating the service is healthy.",
            "content": {
                "application/json": {
                    "example": {"status": "ok", "message": "Service is running"}
                }
            },
        },
    },
)
def health_check(request: Request):
    """
    Health check endpoint.

    Logs the request and returns the service health status.
    """
    logger.info("Health check endpoint called", extra={"request_id": request.state.request_id})
    return {"status": "ok", "message": "Service is running"}