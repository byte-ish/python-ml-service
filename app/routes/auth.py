import requests
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.jwt import create_jwt_token  # Importing the function to generate JWT

router = APIRouter()

JIRA_BASE_URL = "https://byteit.atlassian.net/"  # Update with your Jira domain

class JiraLoginRequest(BaseModel):
    email: str
    api_token: str

@router.post("/jira-login", tags=["Authentication"], summary="Authenticate with Jira", description="Authenticate using Jira credentials (email + API token) to receive a JWT token for further API calls.")
def jira_login(credentials: JiraLoginRequest):
    """
    Authenticate users using Jira credentials (email + API token).

    Args:
        credentials (JiraLoginRequest): The user's Jira credentials.

    Returns:
        dict: The issued JWT token if authentication is successful.
    """
    # Jira API URL to get the current user's details
    jira_url = f"{JIRA_BASE_URL}/rest/api/3/myself"

    # Making an API request to Jira to authenticate the user
    response = requests.get(
        jira_url,
        auth=(credentials.email, credentials.api_token)  # Jira basic authentication
    )

    if response.status_code == 200:
        # Successful authentication, generate JWT token
        jwt_token = create_jwt_token({"sub": credentials.email})  # Encode email as subject
        return {"access_token": jwt_token, "token_type": "Bearer"}
    else:
        # Authentication failed
        raise HTTPException(status_code=401, detail="Invalid Jira credentials.")