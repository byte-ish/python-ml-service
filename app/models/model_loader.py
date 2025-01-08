"""
Module to load models dynamically using the ModelRegistry.
"""

from app.models.model_registry import ModelRegistry

def load_model(model_id: str):
    """
    Load a model using the ModelRegistry.

    Args:
        model_id (str): Unique identifier for the model.

    Returns:
        Any: Loaded ML model.

    Raises:
        KeyError: If the model ID is not registered.
        FileNotFoundError: If the model file is missing.
        RuntimeError: If there is an error during loading.
    """
    return ModelRegistry.load_model(model_id)
