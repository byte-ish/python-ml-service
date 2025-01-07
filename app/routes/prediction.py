# app/routes/prediction.py
from fastapi import APIRouter, HTTPException, Request, Depends
from app.schemas import ModelAInput, ModelAOutput, ModelBInput, ModelBOutput
from app.services.prediction_service import predict
from app.logger import get_logger
from app.utils.jwt import verify_jwt_token

router = APIRouter()
logger = get_logger(__name__)

@router.post("/predict/model_a", response_model=ModelAOutput)
def predict_model_a(data: ModelAInput, request: Request):
    request_id = request.state.request_id
    logger.info(f"Prediction request for Model A. Request ID: {request_id}")

    try:
        result = predict(data.dict(), model_id="model_a", model_type="sklearn_model_a", request_id=request_id)
        return {"sentiment": result}
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")


@router.post("/predict/model_b", response_model=ModelBOutput)
def predict_model_b(data: ModelBInput, request: Request):
    request_id = request.state.request_id
    logger.info(f"Prediction request for Model B. Request ID: {request_id}")

    try:
        result = predict(data.dict(), model_id="model_b", model_type="sklearn_model_b", request_id=request_id)
        return {"sum": result}
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")