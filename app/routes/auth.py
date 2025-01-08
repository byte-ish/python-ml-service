"""
Routes for authentication.
Provides functionality to authenticate with Jira and issue JWT tokens.
"""

import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel  # Ensure Pydantic is correctly imported and installed
from app.utils.jwt import create_jwt_token  # Importing the function to generate JWT

router = APIRouter()

JIRA_BASE_URL = "https://byteit.atlassian.net/"  # Update with your Jira domain


class JiraLoginRequest(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Schema for Jira login request containing email and API token.
    """
    email: str
    api_token: str


@router.post(
    "/jira-login",
    tags=["Authentication"],
    summary="Authenticate with Jira",
    description=(
        "Authenticate using Jira credentials (email + API token) to receive a "
        "JWT token for further API calls."
    ),
)
def jira_login(credentials: JiraLoginRequest):
    """
    Authenticate users using Jira credentials (email + API token).

    Args:
        credentials (JiraLoginRequest): The user's Jira credentials.

    Returns:
        dict: The issued JWT token if authentication is successful.

    Raises:
        HTTPException: If Jira authentication fails.
    """
    jira_url = f"{JIRA_BASE_URL}/rest/api/3/myself"

    try:
        # Making an API request to Jira to authenticate the user
        response = requests.get(
            jira_url,
            auth=(credentials.email, credentials.api_token),  # Jira basic authentication
            timeout=10  # Adding a timeout to prevent indefinite hanging
        )

        if response.status_code == 200:
            # Successful authentication, generate JWT token
            jwt_token = create_jwt_token({"sub": credentials.email})  # Encode email as subject
            return {"access_token": jwt_token, "token_type": "Bearer"}

        raise HTTPException(status_code=401, detail="Invalid Jira credentials.")
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Jira: {e}") from e
