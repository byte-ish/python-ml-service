"""
Logger setup for the microservice.
"""
import logging
from logging.handlers import RotatingFileHandler

def setup_logger() -> logging.Logger:
    """
    Configures and returns a logger instance.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("microservice_logger")
    logger.setLevel(logging.DEBUG)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # File Handler with rotation
    file_handler = RotatingFileHandler("microservice.log", maxBytes=5 * 1024 * 1024, backupCount=3)
    file_handler.setLevel(logging.DEBUG)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Adding Handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

# Initialize logger
LOGGER = setup_logger()