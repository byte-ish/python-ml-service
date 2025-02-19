from fastapi import FastAPI, Request
import time
import uuid
from prometheus_fastapi_instrumentator import Instrumentator
from app.logger import get_logger
from app.routes.healthcheck import router as health_router
from app.routes.prediction import router as prediction_router
from app.routes.async_prediction import router as async_router
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
async def log_request_time_middleware(request: Request, call_next):
    """
    Middleware to log execution time for all requests.
    """
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id

    start_time = time.perf_counter()
    response = await call_next(request)
    end_time = time.perf_counter()

    process_time = end_time - start_time
    logger.info(
        f"Request ID: {request_id} | Path: {request.url.path} | Time Taken: {process_time:.4f} sec",
        extra={"request_id": request_id},
    )

    response.headers["X-Request-ID"] = request_id
    response.headers["X-Response-Time"] = str(process_time)

    return response


@app.on_event("startup")
async def startup_event():
    """
    Actions to perform during the startup of the application.
    """
    logger.info("Application startup: Loading model configurations.")

    try:
        ModelRegistry.load_config("app/config/models_config.json")
        logger.info("All models registered successfully.")
    except Exception as e:
        logger.error(f"Error during model registration: {e}")

# Include routers
app.include_router(health_router)
app.include_router(prediction_router)
app.include_router(auth_router, prefix="/auth")
app.include_router(async_router, prefix="/async")

if __name__ == "__main__":
    import uvicorn

    logger.info(f"Application configuration: {Config.display_config()}")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
