# app/models/model_registry.py
import pickle
from threading import Lock
from app.logger import get_logger

logger = get_logger(__name__)

class ModelRegistry:
    """
    A registry to manage configurations and instances of multiple ML models.
    """
    _registry = {}  # To store model configurations
    _models = {}  # To cache loaded models
    _lock = Lock()

    @classmethod
    def register_model(cls, model_id: str, model_path: str):
        """
        Register a model with its configuration.

        Args:
            model_id (str): Unique identifier for the model.
            model_path (str): File path to the model.
        """
        with cls._lock:
            if model_id in cls._registry:
                logger.warning(f"Model '{model_id}' is already registered. Overwriting.")
            cls._registry[model_id] = model_path
            logger.info(f"Model registered: {model_id} at {model_path}")

    @classmethod
    def load_model(cls, model_id: str):
        """
        Load a model dynamically. Uses caching for already-loaded models.

        Args:
            model_id (str): Unique identifier for the model.

        Returns:
            Any: Loaded ML model.

        Raises:
            KeyError: If the model ID is not registered.
            Exception: If there is an error loading the model.
        """
        with cls._lock:
            if model_id in cls._models:
                logger.info(f"Model '{model_id}' loaded from cache.")
                return cls._models[model_id]

            if model_id not in cls._registry:
                error_message = f"Model '{model_id}' is not registered."
                logger.error(error_message)
                raise KeyError(error_message)

            model_path = cls._registry[model_id]
            try:
                with open(model_path, "rb") as file:
                    model = pickle.load(file)
                    cls._models[model_id] = model
                    logger.info(f"Model '{model_id}' successfully loaded from {model_path}.")
                    return model
            except FileNotFoundError:
                error_message = f"Model file not found at {model_path} for model ID '{model_id}'."
                logger.error(error_message)
                raise FileNotFoundError(error_message)
            except Exception as e:
                error_message = f"Error loading model '{model_id}': {str(e)}"
                logger.error(error_message)
                raise RuntimeError(error_message)

    @classmethod
    def list_registered_models(cls):
        """
        List all registered models in the registry.

        Returns:
            dict: A dictionary of registered models and their paths.
        """
        with cls._lock:
            return cls._registry.copy()