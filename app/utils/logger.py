"""
Logger module for structured JSON logging with contextual information.
Includes a custom JSON formatter and a context filter for request-level data.
"""

import logging
import logging.handlers
import json
from fastapi.logger import logger as fastapi_logger
from app.config.config import Config


class CustomJSONFormatter(logging.Formatter):
    """
    Custom JSON formatter for structured logging.
    Formats log messages into JSON with additional contextual fields.
    """

    def format(self, record):
        """
        Format the log record as JSON.

        Args:
            record (logging.LogRecord): Log record to be formatted.

        Returns:
            str: JSON-formatted log message.
        """
        log_record = {
            "timestamp": self.formatTime(record, "%Y-%m-%dT%H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "request_id": getattr(record, "request_id", "N/A"),  # Default to "N/A" if unset
        }
        # Include any `extra` fields passed explicitly
        if hasattr(record, "extra") and isinstance(record.extra, dict):
            log_record.update(record.extra)
        return json.dumps(log_record)


class ContextFilter(logging.Filter):
    """
    A logging filter that adds contextual information like `request_id` to log records.
    """

    def __init__(self):
        """
        Initialize the ContextFilter with no request ID.
        """
        super().__init__()
        self.request_id = None

    def set_request_id(self, request_id):
        """
        Sets the `request_id` for the current context.

        Args:
            request_id (str): Unique request ID to associate with log records.
        """
        self.request_id = request_id

    def filter(self, record):
        """
        Adds the `request_id` to the log record.

        Args:
            record (logging.LogRecord): Log record to filter.

        Returns:
            bool: Always True to include the record.
        """
        record.request_id = self.request_id or "N/A"  # Default to "N/A" if unset
        return True


# Create a global instance of the context filter
context_filter = ContextFilter()


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

    # Add context filter to include `request_id`
    logger.addFilter(context_filter)

    return logger
