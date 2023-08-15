"""Interfaces for auth module."""
from .login import ILoginRequest
from .login import ILoginResponse
from .logup import ILogupRequest
from .logup import ILogupResponse
from .token_request import ITokenRequest


__all__ = [
    "ILogupRequest",
    "ILogupResponse",
    "ILoginRequest",
    "ILoginResponse",
    "ITokenRequest",
]
