"""
Service for handling prediction requests.
"""
from app.models.model_registry import ModelRegistry
from app.config.registry import ProcessorRegistry
from app.logger import get_logger

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
    logger.info(f"Starting prediction. Request ID: {request_id} | Model ID: {model_id}")

    # Load the model
    try:
        model = ModelRegistry.load_model(model_id)
        model_type = ModelRegistry.get_model_type(model_id)
        logger.info(f"Model '{model_id}' successfully loaded with type '{model_type}'.")
    except Exception as e:
        logger.error(f"Error loading model '{model_id}': {e}")
        raise ValueError(f"Error loading model '{model_id}': {e}")

    # Preprocess the input
    try:
        preprocessor = ProcessorRegistry.get_preprocessor(model_type)
        processed_input = preprocessor.preprocess({"input": input_data["input"]})
        logger.info(f"Input data preprocessed successfully: {processed_input}")
    except Exception as e:
        logger.error(f"Error during preprocessing: {e}")
        raise ValueError(f"Error during preprocessing: {e}")

    # Perform inference
    try:
        raw_prediction = model.predict(processed_input["features"])
        logger.info(f"Model inference completed. Raw prediction: {raw_prediction}")
    except Exception as e:
        logger.error(f"Error during inference: {e}")
        raise ValueError(f"Error during inference: {e}")

    # Postprocess the output
    try:
        postprocessor = ProcessorRegistry.get_postprocessor(model_type)
        prediction = postprocessor.postprocess(raw_prediction)
        logger.info(f"Prediction postprocessed successfully: {prediction}")
        return prediction
    except Exception as e:
        logger.error(f"Error during postprocessing: {e}")
        raise ValueError(f"Error during postprocessing: {e}")