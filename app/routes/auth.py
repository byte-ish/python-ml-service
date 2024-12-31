"""
Authentication routes for handling user login and token generation.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.jwt import create_jwt_token

router = APIRouter()

# Dummy user database
USER_DB = {
    "testuser": {"username": "testuser", "password": "testpassword"}
}

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login", tags=["Authentication"])
def login(credentials: LoginRequest):
    """
    Authenticate user and issue a JWT.

    Args:
        credentials (LoginRequest): User's login credentials.

    Returns:
        dict: The issued JWT token.
    """
    user = USER_DB.get(credentials.username)
    if not user or user["password"] != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    token = create_jwt_token({"sub": credentials.username})
    return {"access_token": token, "token_type": "Bearer"}