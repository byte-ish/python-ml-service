"""
Configuration module for managing environment variables and settings.
"""

import os
from dotenv import load_dotenv

# Determine the current environment (default to development)
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Load the appropriate .env file based on the environment
dotenv_file = f".env.{ENVIRONMENT}"
if not load_dotenv(dotenv_file):
    # Fall back to a default .env file if environment-specific file is not found
    load_dotenv(".env")

class Config:
    """
    Configuration settings for the application.
    """

    # Application environment (e.g., development, staging, production)
    ENVIRONMENT: str = ENVIRONMENT

    # Logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Path to the serialized machine learning model
    MODEL_PATH: str = os.getenv("MODEL_PATH", "app/models/default_model.pkl")

    # API key for authenticating requests
    API_KEY: str = os.getenv("API_KEY", "defaultapikey")

    @classmethod
    def display_config(cls):
        """
        Print the current configuration for debugging purposes.

        Returns:
            dict: The current configuration settings.
        """
        return {
            "ENVIRONMENT": cls.ENVIRONMENT,
            "LOG_LEVEL": cls.LOG_LEVEL,
            "MODEL_PATH": cls.MODEL_PATH,
            "API_KEY": "********",  # Mask API key for display
        }