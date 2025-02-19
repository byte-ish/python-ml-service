"""
In-memory async task handler for ML Predictions.
"""

import asyncio
from app.models.model_registry import ModelRegistry
from app.config.registry import ProcessorRegistry
from app.config.config import TaskStore
from app.logger import get_logger

logger = get_logger(__name__)

async def async_predict_task(task_id: str, input_data: dict, model_id: str):
    """
    Simulates an asynchronous ML model prediction.
    """
    logger.info(f"Started async prediction for Task ID: {task_id}")

    try:
        # Load model
        model = ModelRegistry.load_model(model_id)
        model_type = ModelRegistry.get_model_type(model_id)

        # Preprocess input
        preprocessor = ProcessorRegistry.get_preprocessor(model_type)
        processed_input = preprocessor.preprocess({"input": input_data["input"]})

        # Simulate async inference (e.g., I/O wait)
        await asyncio.sleep(2)  # Simulating ML computation delay

        # Perform inference
        raw_prediction = model.predict(processed_input["features"])

        # Postprocess result
        postprocessor = ProcessorRegistry.get_postprocessor(model_type)
        prediction = postprocessor.postprocess(raw_prediction)

        # Store task result
        TaskStore.update_task(task_id, "completed", prediction)
        logger.info(f"Async prediction completed for Task ID: {task_id}")

    except Exception as e:
        TaskStore.update_task(task_id, "failed", str(e))
        logger.error(f"Prediction failed for Task ID: {task_id} - {e}")
