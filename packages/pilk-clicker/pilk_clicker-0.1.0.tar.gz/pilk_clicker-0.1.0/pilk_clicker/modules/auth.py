"""Auth module"""
from httpx import post

from pilk_clicker.interfaces.auth import ILoginRequest
from pilk_clicker.interfaces.auth import ILoginResponse
from pilk_clicker.interfaces.auth import ILogupRequest
from pilk_clicker.interfaces.auth import ILogupResponse
from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.urls import ApiUrls


class Auth:
    """Auth module"""

    @staticmethod
    def login(credentials: ILoginRequest) -> ILoginResponse:
        """Login to the api

        :param credentials: Login request model
        :return: Login response model
        """
        response = post(ApiUrls.URL_AUTH_LOGIN, json=credentials.model_dump())
        response.raise_for_status()
        return ILoginResponse(**response.json())

    @staticmethod
    def logout(credentials: ITokenRequest) -> None:
        """Logout from the api

        :param credentials: Token request model
        """
        response = post(
            ApiUrls.URL_AUTH_LOGOUT,
            headers={"Authorization": f"Token {credentials.authorization}"},
        )
        response.raise_for_status()

    @staticmethod
    def logup(credentials: ILogupRequest) -> ILogupResponse:
        """Logup to the api

        :param credentials: Logup request model
        :return: Logup response model
        """
        response = post(ApiUrls.URL_USERS, json=credentials.model_dump())
        response.raise_for_status()
        return ILogupResponse(**response.json())
