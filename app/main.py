"""
Main module for the ML Microservice application.
Initializes the FastAPI application, includes routes, and sets up middleware.
"""

import traceback
import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator
from app.utils.logger import get_logger, context_filter
from app.routes.healthcheck import router as health_router
from app.routes.prediction import router as prediction_router
from app.routes.auth import router as auth_router
from app.models.model_registry import ModelRegistry
from app.config.config import Config

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
    Middleware to add a unique request ID to each incoming request and log it.
    """
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    context_filter.set_request_id(request_id)  # Set `request_id` in the logger context
    logger.info("Request ID %s assigned to incoming request.", request_id)  # Lazy formatting
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    context_filter.set_request_id(None)  # Clear the context after the request
    return response


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """
    Handles all unexpected exceptions and logs the stack trace.
    """
    logger.error(
        "Unexpected error: %s | Request ID: %s\nTraceback: %s",
        str(exc),
        request.state.request_id,
        traceback.format_exc(),
    )
    return JSONResponse(
        status_code=500,
        content={
            "error": "An unexpected error occurred. Please try again later.",
            "request_id": request.state.request_id,
        },
    )


# In app/main.py
@app.on_event("startup")
async def startup_event():
    """
    Actions to perform during the startup of the application.
    """
    logger.info("Application startup: Loading model configurations.")
    logger.info("Authentication enabled: %s", Config.ENABLE_AUTHENTICATION)

    try:
        ModelRegistry.load_config("app/config/models_config.json")
        total_models = len(ModelRegistry.list_registered_models())
        logger.info("All models registered successfully. Total models: %d", total_models)
    except RuntimeError as e:
        logger.error("Error during model registration: %s", e)


# Include routers for various functionalities
app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(auth_router, prefix="/auth")

if __name__ == "__main__":
    import uvicorn

    logger.info("Application configuration: %s", Config.display_config())  # Lazy formatting
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
