"""
Service for handling prediction requests.
"""

import time
from app.models.model_registry import ModelRegistry
from app.config.registry import ProcessorRegistry
from app.utils.logger import get_logger
from app.utils.metrics import PREDICTION_RESPONSE_TIME

logger = get_logger(__name__)


def predict(input_data: dict, model_id: str, request_id: str):
    """
    Perform prediction using the specified model, preprocessor, and postprocessor.

    Args:
        input_data (dict): The input data for the prediction.
        model_id (str): The ID of the model to use.
        request_id (str): Unique identifier for the request.

    Returns:
        dict: Postprocessed prediction result.
    """
    logger.info("Starting prediction. Request ID: %s | Model ID: %s", request_id, model_id)
    start_time = time.time()

    try:
        # Load the model
        try:
            model = ModelRegistry.load_model(model_id)
            model_type = ModelRegistry.get_model_type(model_id)
            logger.info("Model '%s' successfully loaded with type '%s'.", model_id, model_type)
        except Exception as e:
            logger.error("Error loading model '%s': %s", model_id, str(e))
            raise ValueError(f"Error loading model '{model_id}': {e}") from e

        # Preprocess the input
        try:
            preprocessor = ProcessorRegistry.get_preprocessor(model_type)
            processed_input = preprocessor.preprocess({"input": input_data["input"]})
            logger.info("Input data preprocessed successfully: %s", processed_input)
        except Exception as e:
            logger.error("Error during preprocessing: %s", str(e))
            raise ValueError(f"Error during preprocessing: {e}") from e

        # Perform inference
        try:
            raw_prediction = model.predict(processed_input["features"])
            logger.info("Model inference completed. Raw prediction: %s", raw_prediction)
        except Exception as e:
            logger.error("Error during inference: %s", str(e))
            raise ValueError(f"Error during inference: {e}") from e

        # Postprocess the output
        try:
            postprocessor = ProcessorRegistry.get_postprocessor(model_type)
            prediction = postprocessor.postprocess(raw_prediction)
            logger.info("Prediction postprocessed successfully: %s", prediction)
            return prediction
        except Exception as e:
            logger.error("Error during postprocessing: %s", str(e))
            raise ValueError(f"Error during postprocessing: {e}") from e

    finally:
        # Observe response time in the Prometheus histogram
        response_time = time.time() - start_time
        logger.info("Prediction response time observed: %f seconds.", response_time)
        PREDICTION_RESPONSE_TIME.observe(response_time)
