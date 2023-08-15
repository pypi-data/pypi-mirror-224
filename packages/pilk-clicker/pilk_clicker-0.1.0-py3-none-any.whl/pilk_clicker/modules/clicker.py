"""Clicker module"""
from typing import List

from httpx import get
from httpx import put

from pilk_clicker.interfaces.auth import ITokenRequest
from pilk_clicker.interfaces.clicker import IClickerDetailResponse
from pilk_clicker.interfaces.clicker import IClickerSaveRequest
from pilk_clicker.interfaces.clicker import IClickerSaveResponse
from pilk_clicker.interfaces.clicker import ITopListResponse
from pilk_clicker.urls import ApiUrls


class Clicker:
    @staticmethod
    def clicker_detail(credentials: ITokenRequest) -> IClickerDetailResponse:
        """Get clicker detail

        :param credentials: Token request model
        :return: Clicker detail response model
        """
        response = get(
            ApiUrls.URL_CLICKER,
            headers={"Authorization": f"Token {credentials.authorization}"},
        )
        response.raise_for_status()
        return IClickerDetailResponse(**response.json())

    @staticmethod
    def top_list(credentials: ITokenRequest) -> List[ITopListResponse]:
        """Get top list

        :param credentials: Token request model
        :return: Top list response model
        """
        response = get(
            ApiUrls.URL_TOP_LIST,
            headers={"Authorization": f"Token {credentials.authorization}"},
        )
        response.raise_for_status()
        return [ITopListResponse(**item) for item in response.json()]

    @staticmethod
    def save_clicker(
        data: IClickerSaveRequest, credentials: ITokenRequest
    ) -> IClickerSaveResponse:
        """Save clicker

        :param data: Clicker save request model
        :param credentials: Token request model
        :return: Clicker save response model
        """
        response = put(
            ApiUrls.URL_SAVE_CLICKER,
            json=data.model_dump(),
            headers={"Authorization": f"Token {credentials.authorization}"},
        )
        response.raise_for_status()
        return IClickerSaveResponse(**response.json())
