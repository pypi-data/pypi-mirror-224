"""Shop interfaces"""
from pydantic import BaseModel


class ISaveItemRequest(BaseModel):
    """Save item request model"""

    id: int
    amount: int


class ISaveItemResponse(BaseModel):
    """Save item response model"""

    id: int
    name: str
    amount: int
    price: int
    base_price: int
    arcoins_per_seconds: float
    arcoins_per_click: int
    image: str


class IShopUserResponse(BaseModel):
    """Shop user response model"""

    id: int
    name: str
    amount: int
    price: int
    base_price: int
    arcoins_per_seconds: float
    arcoins_per_click: int
    image: str
