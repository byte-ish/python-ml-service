"""
Utility functions for creating and verifying JWT tokens.
"""

from datetime import datetime, timedelta
from jose import jwt
from app.config import Config

def create_jwt_token(data: dict):
    """
    Generate a JWT token.

    Args:
        data (dict): The data to encode into the token.

    Returns:
        str: The generated JWT token.
    """
    expiration = datetime.utcnow() + timedelta(minutes=Config.JWT_EXPIRATION_MINUTES)
    payload = {**data, "exp": expiration}
    token = jwt.encode(payload, Config.JWT_SECRET_KEY, algorithm=Config.JWT_ALGORITHM)
    return token

def verify_jwt_token(token: str):
    """
    Validate a JWT token and decode its payload.

    Args:
        token (str): The JWT token to validate.

    Returns:
        dict: The decoded payload if valid.

    Raises:
        jwt.JWTError: If the token is invalid or expired.
    """
    payload = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=[Config.JWT_ALGORITHM])
    return payload