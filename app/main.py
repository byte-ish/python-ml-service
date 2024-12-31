"""
Main module for the ML Microservice application.
Initializes the FastAPI application, includes routes, and sets up middleware.
"""

from fastapi import FastAPI, Request
import uuid
from app.logger import get_logger
from app.routes.healthcheck import router as health_router
from app.routes.prediction import router as prediction_router
from app.config import Config

# Initialize FastAPI app
app = FastAPI(
    title="ML Model Microservice",
    version="1.0",
    description="A microservice for ML model inference and health checks."
)

# Initialize logger
logger = get_logger(__name__)


@app.middleware("http")
async def add_request_id_middleware(request: Request, call_next):
    """
    Middleware to add a unique request ID to each incoming request.
    The request ID is included in logs and returned in the response headers.

    Args:
        request (Request): The incoming HTTP request.
        call_next (Callable): The next middleware or route handler.

    Returns:
        Response: The HTTP response with the request ID header.
    """
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    logger.info("Received request", extra={"request_id": request_id})

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


# Include routes from the routes package
app.include_router(health_router)
app.include_router(prediction_router)


# Debugging: Print routes on startup for verification
@app.on_event("startup")
async def print_routes():
    """
    Prints the list of registered routes for debugging during startup.
    """
    logger.info("Application startup: Printing registered routes.")
    for route in app.routes:
        logger.info(f"Route: {route.path} -> {route.name}")


if __name__ == "__main__":
    import uvicorn

    # Print application configuration for debugging
    logger.info(f"Application configuration: {Config.display_config()}")

    # Run the FastAPI application
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)