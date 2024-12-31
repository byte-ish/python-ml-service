"""
Main module for the ML Microservice application.
Initializes the FastAPI application, includes routes, middleware, and authentication.
"""

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security.api_key import APIKeyHeader
import traceback
import uuid
from app.logger import get_logger
from app.routes.healthcheck import router as health_router
from app.routes.prediction import router as prediction_router
from app.exceptions import PredictionError, ServiceError
from app.config import Config

# Initialize FastAPI app
app = FastAPI(
    title="ML Model Microservice",
    version="1.0",
    description="A microservice for ML model inference and health checks.",
)

# Initialize logger
logger = get_logger(__name__)

# API key authentication
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)


def validate_api_key(api_key: str = Depends(api_key_header)):
    """
    Validate the provided API key against the configured value.
    """
    if api_key != Config.API_KEY:
        logger.warning("Unauthorized access attempt with invalid API key.")
        raise HTTPException(status_code=401, detail="Invalid API key.")
    return api_key


@app.middleware("http")
async def add_request_id_middleware(request: Request, call_next):
    """
    Middleware to add a unique request ID to each incoming request.
    """
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    logger.info(f"Request ID {request_id} assigned to incoming request.", extra={"request_id": request_id})
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


@app.exception_handler(PredictionError)
async def prediction_error_handler(request: Request, exc: PredictionError):
    """
    Handles PredictionError exceptions and returns a standardized error response.
    """
    logger.error(
        f"Prediction error: {exc.detail} | Request ID: {request.state.request_id}"
    )
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "request_id": request.state.request_id},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Handles all unexpected exceptions and logs the stack trace.
    """
    logger.error(
        f"Unexpected error: {str(exc)} | Request ID: {request.state.request_id}\n"
        f"Traceback: {traceback.format_exc()}"
    )
    return JSONResponse(
        status_code=500,
        content={
            "error": "An unexpected error occurred. Please try again later.",
            "request_id": request.state.request_id,
        },
    )


# Include routes from the routes package
# Add the API key validation dependency for secure routes
app.include_router(health_router, dependencies=[Depends(validate_api_key)])
app.include_router(prediction_router, dependencies=[Depends(validate_api_key)])


# Example of a secure health check endpoint
@app.get("/secure-health", dependencies=[Depends(validate_api_key)])
def secure_health():
    """
    A secure health check endpoint requiring API key authentication.
    """
    return {"status": "ok", "message": "Secure health endpoint is operational."}


if __name__ == "__main__":
    import uvicorn

    logger.info(f"Application configuration: {Config.display_config()}")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)