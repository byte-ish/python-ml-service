from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.security.api_key import APIKeyHeader
from app.schemas import PredictionInput, PredictionResponse
from app.services.prediction_service import predict
from app.logger import get_logger
from app.config import Config

router = APIRouter()
logger = get_logger(__name__)

# API key dependency
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def validate_api_key(api_key: str = Depends(api_key_header)):
    """
    Validate the provided API key.
    """
    if api_key != Config.API_KEY:
        logger.warning("Unauthorized access attempt with invalid API key.")
        raise HTTPException(status_code=401, detail="Invalid API key.")
    return api_key

@router.post(
    "/predict",
    tags=["Prediction"],
    summary="Prediction Endpoint",
    description=(
        "Takes a string input and returns a prediction as a string based on the pre-trained ML model."
    ),
    response_model=PredictionResponse,
    responses={
        400: {
            "description": "Invalid input or prediction error.",
            "content": {
                "application/json": {
                    "example": {"detail": "Prediction failed: Invalid input"}
                }
            },
        },
    },
    dependencies=[Depends(validate_api_key)],
)
def get_prediction(data: PredictionInput, request: Request):
    """
    Prediction endpoint.

    Logs the request and prediction outcome or errors.

    Args:
        data (PredictionInput): The input data for prediction.
        request (Request): The incoming HTTP request.

    Returns:
        dict: The prediction result.
    """
    request_id = request.state.request_id
    logger.info("Prediction endpoint called", extra={"request_id": request_id})
    try:
        result = predict(data, request_id)
        logger.info(f"Prediction successful: {result}", extra={"request_id": request_id})
        return {"prediction": result}
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}", extra={"request_id": request_id})
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")