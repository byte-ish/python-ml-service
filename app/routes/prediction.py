from fastapi import APIRouter, HTTPException
from app.schemas import PredictionInput
from app.services.prediction_service import predict

router = APIRouter()

@router.post("/predict", tags=["Prediction"])
def get_prediction(data: PredictionInput):
    """Prediction endpoint."""
    try:
        result = predict(data)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction failed: {str(e)}")