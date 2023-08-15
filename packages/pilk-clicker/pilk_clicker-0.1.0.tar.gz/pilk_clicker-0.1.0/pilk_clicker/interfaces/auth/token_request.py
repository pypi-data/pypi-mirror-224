"""Token request interface"""
from pydantic import BaseModel


class ITokenRequest(BaseModel):
    """Token request model"""

    authorization: str
