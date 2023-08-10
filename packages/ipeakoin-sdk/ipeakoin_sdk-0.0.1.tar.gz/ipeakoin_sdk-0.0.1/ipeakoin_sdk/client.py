from typing import Optional, overload, Union, Type

from ipeakoin_sdk.constant import Constant
from ipeakoin_sdk.models.api_response import ApiResponse
from ipeakoin_sdk.models.test_data import TestData
from ipeakoin_sdk.request import Request


class Client:

    def __init__(self, app_id: str, app_secret: str, base_url: Optional[str] = None):
        self._app_id = app_id
        self._app_secret = app_secret
        self._base_url = base_url or Constant.static_base_url
        pass

    @overload
    def get_code(self) -> ApiResponse[Type[TestData]]: ...

    @overload
    def get_code(self, state: str) -> ApiResponse[Type[TestData]]: ...

    @overload
    def get_code(self, state: int) -> ApiResponse[Type[TestData]]: ...

    def get_code(self, state: Union[str, int] = None) -> ApiResponse[Type[TestData]]:
        url = self._base_url + "/open-api/oauth/authorize"
        params = {
            "clientId": self._app_id,
            "state": state,
        }

        response = Request.request("GET", url, TestData, params)
        return response

    pass


if __name__ == '__main__':
    client = Client(app_id="ipeakoin1ab59eccfbc78d1b2", app_secret="93fc39d77ef6a3a7b5f26b83fbbebe81",
                    base_url="http://127.0.0.1:3000")

    res = client.get_code()

    print(res.content.id)
