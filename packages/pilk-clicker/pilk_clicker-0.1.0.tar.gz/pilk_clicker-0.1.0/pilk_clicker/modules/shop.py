"""Shop module"""
from typing import List

from httpx import get
from httpx import put

from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.interfaces.shop import ISaveItemRequest
from pilk_clicker.interfaces.shop import ISaveItemResponse
from pilk_clicker.interfaces.shop import IShopUserResponse
from pilk_clicker.urls import ApiUrls


class Shop:
    """Shop class"""

    @staticmethod
    def shop_user(credentials: ITokenRequest) -> List[IShopUserResponse]:
        """Get shop user

        :param credentials: Token request model
        :return: Shop user response model
        """
        response = get(
            ApiUrls.URL_SHOP_USER_DETAIL,
            headers={"Authorization": f"Token {credentials.authorization}"},
        )
        response.raise_for_status()
        return [IShopUserResponse(**item) for item in response.json()]

    @staticmethod
    def save_item(
        data: ISaveItemRequest, credentials: ITokenRequest
    ) -> ISaveItemResponse:
        """Save item

        :param data: Save item request model
        :param credentials: Token request model
        :return: Save item response model
        """
        response = put(
            ApiUrls.URL_SAVE_ITEM,
            json=data.model_dump(),
            headers={"Authorization": f"Token {credentials.authorization}"},
        )
        response.raise_for_status()
        return ISaveItemResponse(**response.json())
