from typing import TypeVar

import requests
from pydantic import BaseModel
from requests import Response

from ipeakoin_sdk.models.api_response import ApiResponse
from ipeakoin_sdk.models.test_data import TestData

T = TypeVar('T')


class Request(object):

    @staticmethod
    def request(method: str, url: str, clazz: T, params: dict = None) -> ApiResponse[T]:
        """
        send request
        :param method: method for the new :class:`Request` object: ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``,
         ``PATCH``, or ``DELETE``.
        :param url: URL for the new :class:`Request` object.
        :param params: (optional) Dictionary
         :param clazz: T
        :return: Response
        """
        # response: Response = requests.request(method=method, url=url, params=params)
        # status_code = response.status_code
        # obj: dict = response.json()
        obj: dict = {
            "code": 0,
            "message1": "12413",
            "error": "121",
            "data": {
                "id": "1231",
                "name": "231321",
                "age": 1
            }
        }

        res = {
            "code": obj.get("code", None),
            "message": obj.get("message", None),
            "content": clazz(**obj.get("data", None))
        }

        return ApiResponse[T](**res)


pass
