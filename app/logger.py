import logging
import logging.handlers
import json
from fastapi.logger import logger as fastapi_logger
from app.config import Config

class CustomJSONFormatter(logging.Formatter):
    """Custom JSON formatter for structured logging."""

    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "request_id": getattr(record, "request_id", None),
        }
        return json.dumps(log_record)


def get_logger(name):
    """
    Sets up and returns a logger with structured JSON logging.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger  # Prevent duplicate handlers

    # Set log level from config
    logger.setLevel(Config.LOG_LEVEL)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(CustomJSONFormatter())
    logger.addHandler(console_handler)

    # Log rotation
    file_handler = logging.handlers.RotatingFileHandler(
        "app_logs.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setFormatter(CustomJSONFormatter())
    logger.addHandler(file_handler)

    # Integrate with FastAPI logger
    fastapi_logger.handlers = logger.handlers
    fastapi_logger.setLevel(Config.LOG_LEVEL)

    return logger