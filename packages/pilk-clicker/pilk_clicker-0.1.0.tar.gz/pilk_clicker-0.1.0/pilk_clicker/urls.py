"""Urls for pilk_clicker api"""
from typing import Final


class ApiUrls:
    """Api urls"""

    _URL: Final = "http://pilk-clicker.ru/api"

    _URL_AUTH: Final = f"{_URL}/auth"
    URL_AUTH_LOGIN: Final = f"{_URL_AUTH}/token/login/"
    URL_AUTH_LOGOUT: Final = f"{_URL_AUTH}/token/logout/"

    URL_USERS: Final = f"{_URL_AUTH}/users/"

    URL_CLICKER: Final = f"{_URL}/clicker/"
    URL_SAVE_CLICKER: Final = f"{_URL}/save_clicker/"
    URL_TOP_LIST: Final = f"{_URL}/top_list/"

    URL_SHOP_USER_DETAIL: Final = f"{_URL}/shop_user_detail/"
    URL_SAVE_ITEM: Final = f"{_URL}/save_item/"
