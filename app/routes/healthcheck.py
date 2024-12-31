from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck", tags=["Health"])
def health_check():
    """Health check endpoint."""
    return {"status": "ok", "message": "Service is running"}