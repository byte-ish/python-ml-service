# app/services/prediction_service.py
from time import time
from app.models.model_loader import load_model
from app.logger import get_logger
from app.config.registry import ProcessorRegistry

logger = get_logger(__name__)

def predict(input_data: dict, model_id: str, model_type: str, request_id: str):
    logger.info(f"Prediction request received for Model ID: {model_id}. Request ID: {request_id}")
    start_time = time()

    try:
        # Load the model
        model = load_model(model_id)
        logger.info(f"Model '{model_id}' loaded successfully for Request ID: {request_id}")

        # Preprocess input
        preprocessor = ProcessorRegistry.get_preprocessor(model_type)
        preprocessed_input = preprocessor.preprocess(input_data)

        # Perform inference
        raw_prediction = model.predict(preprocessed_input["features"])
        logger.info(f"Raw prediction: {raw_prediction}")

        # Postprocess output
        postprocessor = ProcessorRegistry.get_postprocessor(model_type)
        result = postprocessor.postprocess(raw_prediction)

    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}", exc_info=True)
        raise

    total_time = time() - start_time
    logger.info(f"Prediction completed in {total_time:.4f} seconds for Request ID: {request_id}")
    return result