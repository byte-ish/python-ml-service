from app.config.config import Config

def test_config_values():
    assert Config.ENVIRONMENT in ["development", "staging", "production"]
    assert isinstance(Config.LOG_LEVEL, str)
    assert Config.MODEL_PATH.endswith("model.pkl")
    assert Config.JWT_SECRET_KEY
    assert Config.JWT_ALGORITHM == "HS256"
    assert isinstance(Config.JWT_EXPIRATION_MINUTES, int)
