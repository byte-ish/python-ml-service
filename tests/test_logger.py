
from app.utils.logger import get_logger

def test_logger_initialization():
    logger = get_logger("test_logger")
    assert logger.name == "test_logger"
    assert logger.hasHandlers()
