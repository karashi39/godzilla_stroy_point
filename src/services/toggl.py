from enum import Enum

import requests
from requests.auth import HTTPBasicAuth


class _Endpoints(str, Enum):
    ME = "/api/v9/me"
    TIME_ENTRIES = "/api/v9/me/time_entries"
    WORKSPACE_PROJECTS = "/api/v9/workspaces/{workspace_id}/projects"

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
            print(response.status_code)
            raise Exception
        if is_text:
            return {"response": response.text}
        return response.json()

    def get_me(self) -> dict:
        url = self.BASE_URL + _Endpoints.ME
        return self._get(url)

    def get_time_entries(self, start_date: str, end_date: str) -> dict:
        url = (
            self.BASE_URL
            + _Endpoints.TIME_ENTRIES
            + f"?start_date={start_date}&end_date={end_date}"
        )
        return self._get(url)

    def get_workspace_projects(self, workspace_id: int) -> dict:
        url = self.BASE_URL + _Endpoints.WORKSPACE_PROJECTS.format(
            workspace_id=workspace_id
        )
        return self._get(url)
