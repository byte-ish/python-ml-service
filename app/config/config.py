"""
Configuration module for managing environment variables and settings.
"""

import os
from dotenv import load_dotenv

# Determine the current environment (default to development)
DEFAULT_ENVIRONMENT = "development"
ENVIRONMENT = os.getenv("ENVIRONMENT", DEFAULT_ENVIRONMENT)

# Load the appropriate .env file based on the environment
DOTENV_FILE = f".env.{ENVIRONMENT}"
if not load_dotenv(DOTENV_FILE):
    load_dotenv(".env")


class Config:  # pylint: disable=too-few-public-methods
    """
    Configuration settings for the application.
    """

    ENVIRONMENT: str = ENVIRONMENT  # Use the defined ENVIRONMENT variable
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    MODEL_PATH: str = os.getenv("MODEL_PATH", "app/models/default_model.pkl")
    API_KEY: str = os.getenv("API_KEY", "defaultapikey")

    # JWT Authentication Configuration
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "mysecretjwtkey")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_MINUTES: int = int(os.getenv("JWT_EXPIRATION_MINUTES", "30"))

    # Enable or disable authentication
    ENABLE_AUTHENTICATION: bool = os.getenv("ENABLE_AUTHENTICATION", "true").lower() == "true"

    @classmethod
    def display_config(cls):
        """
        Print the current configuration for debugging purposes.

        Returns:
            dict: Configuration settings.
        """
        return {
            "ENVIRONMENT": cls.ENVIRONMENT,
            "LOG_LEVEL": cls.LOG_LEVEL,
            "MODEL_PATH": cls.MODEL_PATH,
            "API_KEY": "********",
            "JWT_SECRET_KEY": "********",
            "JWT_ALGORITHM": cls.JWT_ALGORITHM,
            "JWT_EXPIRATION_MINUTES": cls.JWT_EXPIRATION_MINUTES,
            "ENABLE_AUTHENTICATION": cls.ENABLE_AUTHENTICATION,
        }
