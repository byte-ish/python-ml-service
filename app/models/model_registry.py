import pickle
import json
from threading import Lock
from app.utils.logger import get_logger

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
        logger.info("START: Loading model configurations from JSON file.", extra={"config_path": config_path})
        try:
            with open(config_path, "r") as file:
                config = json.load(file)
                for model in config.get("models", []):
                    cls.register_model(model["id"], model["path"], model["type"])
            total_models = len(cls._registry)
            print("DEBUG: Total models registered:", total_models)
            logger.info(
                "SUCCESS: Model configurations loaded successfully.", extra={"total_models_registered": total_models}
            )
        except Exception as e:
            logger.error(
                f"ERROR: Failed to load model configurations: {e}",
                exc_info=True
            )
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
        logger.info(
            "START: Registering model.",
            extra={"model_id": model_id, "model_path": model_path, "model_type": model_type}
        )
        with cls._lock:
            if model_id in cls._registry:
                logger.warning(f"WARNING: Model '{model_id}' is already registered. Overwriting.")
            cls._registry[model_id] = {"path": model_path, "type": model_type}
            logger.info(
                "SUCCESS: Model registered.",
                extra={"model_id": model_id, "model_path": model_path, "model_type": model_type}
            )

    @classmethod
    def is_registered(cls, model_id: str) -> bool:
        """
        Check if a model is registered in the registry.

        Args:
            model_id (str): Unique identifier for the model.

        Returns:
            bool: True if the model is registered, False otherwise.
        """
        logger.debug(f"Checking if model '{model_id}' is registered.")
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
        logger.info(f"START: Loading model '{model_id}'.")
        with cls._lock:
            if model_id in cls._models:
                logger.info(
                    "SUCCESS: Model loaded from cache.",
                    extra={"model_id": model_id}
                )
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
                    logger.info(
                        "SUCCESS: Model loaded from file.",
                        extra={"model_id": model_id, "model_path": model_path}
                    )
                    return model
            except FileNotFoundError:
                error_message = f"ERROR: Model file not found at {model_path} for model ID '{model_id}'."
                logger.error(error_message)
                raise FileNotFoundError(error_message)
            except Exception as e:
                error_message = f"ERROR: Error loading model '{model_id}': {str(e)}"
                logger.error(error_message, exc_info=True)
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
        logger.debug(f"Fetching model type for model ID '{model_id}'.")
        if model_id not in cls._registry:
            error_message = f"Model '{model_id}' is not registered."
            logger.error(error_message)
            raise KeyError(error_message)
        return cls._registry[model_id]["type"]

    @classmethod
    def list_registered_models(cls):
        """
        List all registered models in the registry.

        Returns:
            dict: A dictionary of registered models and their configurations.
        """
        logger.info("Listing all registered models.")
        with cls._lock:
            return cls._registry.copy()