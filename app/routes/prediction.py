"""
Routes for prediction requests.
"""
from fastapi import APIRouter, HTTPException, Request
from app.schemas.prediction_schema import PredictionInput, PredictionResponse
from app.services.prediction_service import predict
from app.models.model_registry import ModelRegistry
from app.utils.logger import get_logger
from app.utils.metrics import PREDICTION_HIT_COUNTER

router = APIRouter()
logger = get_logger(__name__)


@router.post(
    "/predict/{model_id}",
    tags=["Prediction"],
    response_model=PredictionResponse,
    summary="Prediction Endpoint",
    description="Endpoint for making predictions using different models.",
)
async def get_prediction(model_id: str, data: PredictionInput, request: Request):
    """
    Handle prediction requests based on the specified model_id.

    Args:
        model_id (str): Identifier of the model to use.
        data (PredictionInput): Input data for the prediction.
        request (Request): The incoming request object.

    Returns:
        dict: The prediction result.
    """
    PREDICTION_HIT_COUNTER.inc()  # Increment the custom metric
    request_id = request.state.request_id
    logger.info(f"Prediction request received. Request ID: {request_id} | Model ID: {model_id}")

    if not ModelRegistry.is_registered(model_id):
        logger.error(f"Model '{model_id}' is not registered. Request ID: {request_id}")
        raise HTTPException(status_code=400, detail=f"Model '{model_id}' is not registered.")

    try:
        result = predict(input_data=data.dict(), model_id=model_id, request_id=request_id)
        logger.info(f"Prediction successful. Request ID: {request_id}")
        return {"prediction": result}
    except Exception as e:
        logger.error(f"Prediction failed. Request ID: {request_id} | Error: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")