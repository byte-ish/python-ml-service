import os
from dotenv import load_dotenv

# Load environment variables
# Configuration settings
load_dotenv()

class Config:
    MODEL_PATH = os.getenv("MODEL_PATH", "app/models/model.pkl")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    ENVIRONMENT = os.getenv("ENVIRONMENT", "development")