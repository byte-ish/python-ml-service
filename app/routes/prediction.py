# In app/routes/prediction.py
from fastapi import APIRouter, HTTPException, Request, Depends
from app.schemas.prediction_schema import PredictionInput, PredictionResponse
from app.services.prediction_service import predict
from app.models.model_registry import ModelRegistry
from app.utils.logger import get_logger
from app.utils.metrics import PREDICTION_HIT_COUNTER
from app.utils.jwt import verify_jwt_token
from app.config.config import Config

router = APIRouter()
logger = get_logger(__name__)


def check_authentication(token: str = None):
    """
    Check if authentication is enabled and verify the JWT token.

    Args:
        token (str): The JWT token (optional if authentication is disabled).

    Returns:
        dict: Decoded token payload if authentication is enabled.
        None: If authentication is disabled or no token is provided.
    """
    if not Config.ENABLE_AUTHENTICATION:
        logger.info("Authentication is disabled in the configuration.")
        return None  # Skip authentication if disabled

    if not token:
        raise HTTPException(status_code=401, detail="Authentication token is required.")

    try:
        payload = verify_jwt_token(token)
        logger.info("Token successfully verified: %s", payload)
        return payload
    except Exception as e:
        logger.error("Token verification failed: %s", str(e))
        raise HTTPException(status_code=401, detail="Invalid authentication token.")


@router.post(
    "/predict/{model_id}",
    tags=["Prediction"],
    response_model=PredictionResponse,
    summary="Prediction Endpoint",
    description="Endpoint for making predictions using different models.",
)
async def get_prediction(
    model_id: str,
    data: PredictionInput,
    request: Request,
    token: str = Depends(check_authentication),  # Token validation is conditional
):
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
    request_id = getattr(request.state, "request_id", "N/A")
    logger.info("Prediction request received. Request ID: %s | Model ID: %s", request_id, model_id)

    if not ModelRegistry.is_registered(model_id):
        logger.error("Model '%s' is not registered. Request ID: %s", model_id, request_id)
        raise HTTPException(status_code=400, detail=f"Model '{model_id}' is not registered.")

    try:
        result = predict(input_data=data.dict(), model_id=model_id, request_id=request_id)
        logger.info("Prediction successful. Request ID: %s", request_id)
        return {"prediction": result}
    except Exception as e:
        logger.error("Prediction failed. Request ID: %s | Error: %s", request_id, str(e))
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}") from e

