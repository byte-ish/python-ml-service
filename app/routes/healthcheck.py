from fastapi import APIRouter, Request
from app.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.get("/health", tags=["Health"])
async def health_check(request: Request):
    """Health check endpoint."""
    logger.info("Health check called", extra={"request_id": request.state.request_id})
    return {"status": "ok", "message": "Service is running"}