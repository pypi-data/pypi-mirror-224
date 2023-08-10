from typing import Optional


class ApiException(Exception):
    message: str = None

    # res_headers: Optional[dict[str, any]] = None

    def __init__(self, message: str):
        self.message = message
        # self.res_headers = res_headers
