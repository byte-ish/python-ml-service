"""
Main entry point for the microservice with Prometheus integration.
"""
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.routes import healthcheck, prediction
from app.logger import LOGGER
from app.exception_handler import global_exception_handler

# Initialize the FastAPI app
app = FastAPI(title="Python ML Microservice with Prometheus Metrics")

# Initialize Prometheus metrics
Instrumentator().instrument(app).expose(app)

# Register custom exception handlers
app.add_exception_handler(Exception, global_exception_handler)

@app.on_event("startup")
async def startup_event() -> None:
    """
    Event triggered on application startup.
    """
    LOGGER.info("Starting the FastAPI application...")

@app.on_event("shutdown")
async def shutdown_event() -> None:
    """
    Event triggered on application shutdown.
    """
    LOGGER.info("Shutting down the FastAPI application...")

# Register routes
app.include_router(healthcheck.router)
app.include_router(prediction.router)

@app.get("/")
async def root() -> dict:
    """
    Root endpoint.

    Returns:
        dict: Welcome message.
    """
    LOGGER.info("Root endpoint accessed.")
    return {"message": "Welcome to the Python Microservice"}