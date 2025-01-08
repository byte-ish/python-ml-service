import pickle
import json
from threading import Lock
from app.logger import get_logger

logger = get_logger(__name__)

class ModelRegistry:
    """
    A centralized registry for managing model configurations and loaded models.
    """
    _registry = {}  # To store model configurations
    _models = {}  # To cache loaded models
    _lock = Lock()

    @classmethod
    def load_config(cls, config_path: str):
        """
        Load model configurations from a JSON file.

        Args:
            config_path (str): Path to the JSON configuration file.
        """
        try:
            with open(config_path, "r") as file:
                config = json.load(file)
                for model in config.get("models", []):
                    cls.register_model(model["id"], model["path"], model["type"])
            logger.info("Model configurations loaded successfully.")
        except Exception as e:
            logger.error(f"Error loading model configuration: {e}", exc_info=True)
            raise RuntimeError("Failed to load model configurations.")

    @classmethod
    def register_model(cls, model_id: str, model_path: str, model_type: str):
        """
        Register a model with its configuration.

        Args:
            model_id (str): Unique identifier for the model.
            model_path (str): File path to the model.
            model_type (str): Type of the model (e.g., 'sklearn', 'numerical').
        """
        with cls._lock:
            if model_id in cls._registry:
                logger.warning(f"Model '{model_id}' is already registered. Overwriting.")
            cls._registry[model_id] = {"path": model_path, "type": model_type}
            logger.info(f"Model registered: {model_id} at {model_path} with type '{model_type}'.")

    @classmethod
    def is_registered(cls, model_id: str) -> bool:
        """
        Check if a model is registered in the registry.

        Args:
            model_id (str): Unique identifier for the model.

        Returns:
            bool: True if the model is registered, False otherwise.
        """
        with cls._lock:
            return model_id in cls._registry

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

            model_path = cls._registry[model_id]["path"]
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
    def get_model_type(cls, model_id: str) -> str:
        """
        Get the type of the model.

        Args:
            model_id (str): Unique identifier for the model.

        Returns:
            str: Model type.
        """
        if model_id not in cls._registry:
            raise KeyError(f"Model '{model_id}' is not registered.")
        return cls._registry[model_id]["type"]

    @classmethod
    def list_registered_models(cls):
        """
        List all registered models in the registry.

        Returns:
            dict: A dictionary of registered models and their configurations.
        """
        with cls._lock:
            return cls._registry.copy()