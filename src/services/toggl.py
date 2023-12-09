from enum import Enum

import requests
from requests.auth import HTTPBasicAuth


class _Endpoints(str, Enum):
    ME = "/api/v9/me"

    def __str__(self) -> str:
        return self.value


class Toggl:
    BASE_URL = "https://api.track.toggl.com"

    def __init__(self, api_token: str) -> None:
        self.auth = HTTPBasicAuth(api_token, "api_token")
        self.headers = {"Content-Type": "application/json"}

    def _get(self, url: str, is_text: bool = False) -> dict:
        response = requests.get(url, auth=self.auth, headers=self.headers)

        if not (200 <= response.status_code < 400):
            raise Exception
        if is_text:
            return {"response": response.text}
        return response.json()

    def get_me(self) -> None:
        url = self.BASE_URL + _Endpoints.ME
        response = self._get(url)
        return response
