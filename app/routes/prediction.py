from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer
from app.schemas import PredictionInput, PredictionResponse
from app.services.prediction_service import predict
from app.logger import get_logger
from app.utils.jwt import verify_jwt_token
from app.config import Config

router = APIRouter()
logger = get_logger(__name__)

# Authentication methods
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Validate and decode the JWT from the Authorization header.

    Args:
        token (str): The Bearer token from the Authorization header.

    Returns:
        str: The username from the token payload.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    try:
        payload = verify_jwt_token(token)
        return payload["sub"]
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token.")

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
    response_model=PredictionResponse,
    summary="Prediction Endpoint",
    description="Secured endpoint for making predictions.",
    dependencies=[Depends(get_current_user)],  # Use JWT authentication
)
def get_prediction(data: PredictionInput, request: Request):
    """
    Prediction endpoint secured with JWT authentication.

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