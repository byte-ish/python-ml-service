from fastapi import FastAPI
from app.routes.healthcheck import router as health_router
from app.routes.prediction import router as predict_router
from app.logger import get_logger

app = FastAPI(title="ML Model Microservice", version="1.0")
logger = get_logger(__name__)

# Include routes
app.include_router(health_router)
app.include_router(predict_router)