"""
Configuration module for managing environment variables and settings.
"""

import os
from dotenv import load_dotenv
import asyncio
from collections import deque
from typing import Dict, Any

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

    # JWT Configuration
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "mysecretjwtkey")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION_MINUTES: int = int(os.getenv("JWT_EXPIRATION_MINUTES", 30))

    # In-Memory Task Queue Configuration
    MAX_QUEUE_SIZE: int = int(os.getenv("MAX_QUEUE_SIZE", 100))

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
            "API_KEY": "********",  # Mask sensitive info
            "JWT_SECRET_KEY": "********",  # Mask sensitive info
            "JWT_ALGORITHM": cls.JWT_ALGORITHM,
            "JWT_EXPIRATION_MINUTES": cls.JWT_EXPIRATION_MINUTES,
            "MAX_QUEUE_SIZE": cls.MAX_QUEUE_SIZE
        }


class TaskStore:
    """
    In-memory queue for tracking asynchronous tasks.
    """
    def __init__(self):
        self.queue = deque(maxlen=Config.MAX_QUEUE_SIZE)
        self.tasks: Dict[str, Any] = {}  # Store task status with request_id

    async def add_task(self, request_id: str, task: asyncio.Task):
        """
        Add a task to the queue and track its status.

        Args:
            request_id (str): Unique identifier for the request.
            task (asyncio.Task): The asynchronous task to track.
        """
        self.queue.append(request_id)
        self.tasks[request_id] = {"status": "processing"}

        try:
            result = await task
            self.tasks[request_id] = {"status": "completed", "result": result}
        except Exception as e:
            self.tasks[request_id] = {"status": "failed", "error": str(e)}

    def get_status(self, request_id: str) -> Dict[str, Any]:
        """
        Get the status of a queued request.

        Args:
            request_id (str): The unique request identifier.

        Returns:
            dict: Status and result/error if available.
        """
        return self.tasks.get(request_id, {"status": "not found"})

# Global instance of TaskStore
task_store = TaskStore()
