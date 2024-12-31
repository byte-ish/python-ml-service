"""
Main module for the ML Microservice application.
Initializes the FastAPI application, includes routes, and sets up middleware.
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import traceback
import uuid
from prometheus_fastapi_instrumentator import Instrumentator
from app.logger import get_logger
from app.routes.healthcheck import router as health_router
from app.routes.prediction import router as prediction_router
from app.routes.auth import router as auth_router
from app.config import Config

# Initialize FastAPI app
app = FastAPI(
    title="ML Model Microservice",
    version="1.0",
    description="A microservice for ML model inference and health checks.",
)

# Initialize logger
logger = get_logger(__name__)

# Configure Prometheus Instrumentation BEFORE app startup
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

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

# Include routers for various functionalities
app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(auth_router, prefix="/auth")

if __name__ == "__main__":
    import uvicorn

    logger.info(f"Application configuration: {Config.display_config()}")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)