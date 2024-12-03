"""
Prediction route for the microservice.
"""
import time
from fastapi import APIRouter, HTTPException
from prometheus_client import Counter, Histogram
from app.services.prediction_service import predict
from app.logger import LOGGER

router = APIRouter()

# Define metrics
PREDICTION_COUNTER = Counter(
    "prediction_requests_total", "Total number of prediction requests"
)
PREDICTION_LATENCY = Histogram(
    "prediction_request_latency_seconds", "Latency of prediction requests"
)

@router.post("/predict", tags=["Prediction"])
async def make_prediction(input_data: dict) -> dict:
    """
    Endpoint for making predictions using the ML model.

    Args:
        input_data (dict): Input data for prediction.

    Returns:
        dict: Prediction result.
    """
    start_time = time.time()
    try:
        LOGGER.info("Prediction request received: %s", input_data)
        PREDICTION_COUNTER.inc()  # Increment the counter
        result = predict(input_data)
        LOGGER.info("Prediction result: %s", result)
        return {"prediction": result}
    except KeyError as key_err:
        LOGGER.error("KeyError in prediction: %s", str(key_err), exc_info=True)
        raise HTTPException(status_code=400, detail="Invalid input data") from key_err
    except Exception as exc:
        LOGGER.error("Unhandled error in prediction: %s", str(exc), exc_info=True)
        raise HTTPException(status_code=500, detail="Prediction failed.") from exc
    finally:
        latency = time.time() - start_time
        PREDICTION_LATENCY.observe(latency)  # Record latency