import asyncio
import uuid
from fastapi import APIRouter, BackgroundTasks, HTTPException, Request
from app.logger import get_logger
from app.schemas import PredictionInput
from app.services.prediction_service import predict
from app.config.config import task_store
from app.utils.metrics import ASYNC_PREDICTION_HIT_COUNTER, ASYNC_PREDICTION_RESPONSE_TIME

router = APIRouter()
logger = get_logger(__name__)

async def process_async_prediction(model_id: str, data: PredictionInput, request_id: str):
    """
    Handles async prediction request and stores status.
    """
    logger.info(f"Processing async request {request_id} for model {model_id}")

    try:
        ASYNC_PREDICTION_HIT_COUNTER.inc()  # Track async request count

        with ASYNC_PREDICTION_RESPONSE_TIME.time():  # Track async response time
            result = await asyncio.to_thread(
                predict, input_data=data.dict(), model_id=model_id, request_id=request_id
            )

        return {"request_id": request_id, "prediction": result}
    except Exception as e:
        logger.error(f"Async prediction failed for request {request_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

@router.post("/async-predict/{model_id}", tags=["Prediction"])
async def async_prediction(
        model_id: str,
        data: PredictionInput,
        request: Request,
        background_tasks: BackgroundTasks
):
    """
    Endpoint to handle async prediction requests.
    """
    request_id = str(uuid.uuid4())
    logger.info(f"Received async request {request_id} for model {model_id}")

    task = asyncio.create_task(process_async_prediction(model_id, data, request_id))
    background_tasks.add_task(task_store.add_task, request_id, task)

    return {"request_id": request_id, "status": "processing"}
