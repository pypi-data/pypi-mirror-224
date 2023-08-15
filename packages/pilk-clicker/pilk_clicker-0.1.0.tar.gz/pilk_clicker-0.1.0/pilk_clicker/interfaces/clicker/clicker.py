"""Clicker interfaces"""
from pydantic import BaseModel


class IClickerDetailResponse(BaseModel):
    """Clicker detail response model"""

    username: str
    arcoin_amount: int
    arcoins_per_seconds: int
    arcoins_per_click: int


class IClickerSaveRequest(BaseModel):
    """Clicker save request model"""

    arcoin_amount: int
    arcoins_per_seconds: int
    arcoins_per_click: int


class IClickerSaveResponse(BaseModel):
    """Clicker save response model"""

    arcoin_amount: int
    arcoins_per_seconds: int
    arcoins_per_click: int


class ITopListResponse(BaseModel):
    """Top list model"""

    username: str
    arcoin_amount: int
