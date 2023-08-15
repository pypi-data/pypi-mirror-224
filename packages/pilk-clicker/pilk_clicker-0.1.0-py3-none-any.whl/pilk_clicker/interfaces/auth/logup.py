"""Logup interface"""
from pydantic import BaseModel


class ILogupRequest(BaseModel):
    """Logup request model"""

    username: str
    password: str
    email: str


class ILogupResponse(BaseModel):
    """Logup response model"""

    id: int
    username: str
    email: str
