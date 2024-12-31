import logging
from app.config import Config


def get_logger(name: str):
    """Set up application-wide logger."""
    logger = logging.getLogger(name)
    logger.setLevel(Config.LOG_LEVEL)

    # Console handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger