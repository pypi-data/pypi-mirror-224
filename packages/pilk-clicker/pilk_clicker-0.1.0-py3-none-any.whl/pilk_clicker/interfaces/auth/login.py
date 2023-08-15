"""Login interface"""
from pydantic import BaseModel


class ILoginRequest(BaseModel):
    """Login request model"""

    username: str
    password: str


class ILoginResponse(BaseModel):
    """Login response model"""

    auth_token: str
