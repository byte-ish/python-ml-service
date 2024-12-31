from fastapi import APIRouter, HTTPException, Request
from app.schemas import PredictionInput
from app.services.prediction_service import predict
from app.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.post(
    "/predict",
    tags=["Prediction"],
    summary="Prediction Endpoint",
    description=(
        "Takes a string input and returns a prediction as a string based on the pre-trained ML model."
    ),
    responses={
        200: {
            "description": "Prediction successfully returned.",
            "content": {
                "application/json": {
                    "example": {"prediction": "Processed: This is a sample input for the model."}
                }
            },
        },
        400: {
            "description": "Invalid input or prediction error.",
            "content": {
                "application/json": {
                    "example": {"detail": "Prediction failed: Invalid input"}
                }
            },
        },
    },
)
def get_prediction(data: PredictionInput, request: Request):
    """
    Prediction endpoint.

    Logs the request and prediction outcome or errors.
    """
    try:
        logger.info("Prediction endpoint called", extra={"request_id": request.state.request_id})
        result = predict(data)
        logger.info(
            f"Prediction successful: {result}",
            extra={"request_id": request.state.request_id},
        )
        return {"prediction": result}
    except Exception as e:
        logger.error(
            f"Prediction failed: {str(e)}",
            extra={"request_id": request.state.request_id},
        )
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")