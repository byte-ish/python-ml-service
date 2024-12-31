from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.security.api_key import APIKeyHeader
from app.logger import get_logger
from app.config import Config

router = APIRouter()
logger = get_logger(__name__)

# API key dependency
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def validate_api_key(api_key: str = Depends(api_key_header)):
    """
    Validate the provided API key.
    """
    if api_key != Config.API_KEY:
        logger.warning("Unauthorized access attempt with invalid API key.")
        raise HTTPException(status_code=401, detail="Invalid API key.")
    return api_key

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
    dependencies=[Depends(validate_api_key)],
)
def health_check(request: Request):
    """
    Health check endpoint.

    Logs the request and returns the service health status.
    """
    logger.info("Health check endpoint called", extra={"request_id": request.state.request_id})
    return {"status": "ok", "message": "Service is running"}