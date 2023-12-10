from enum import Enum

import requests


class _Endpoints(str, Enum):
    ISSUES = "/rest/agile/1.0/board/{board_id}/issue"

    def __str__(self) -> str:
        return self.value


class Jira:
    BASE_URL = "https://{domain}.atlassian.net"

    def __init__(self, api_token: str, domain: str) -> None:
        self.headers = {
            "Content-Type": "application/json",
            "X-Atlassian-Token": "no-check",
            "Authorization": f"Basic {api_token}",
        }
        self.BASE_URL = self.BASE_URL.format(domain=domain)

    def _get(self, url: str, is_text: bool = False) -> dict:
        response = requests.get(url, headers=self.headers)

        if not (200 <= response.status_code < 400):
            print(response.status_code)
            raise Exception
        if is_text:
            return {"response": response.text}
        return response.json()

    def get_issues(self, board_id: int, start_at: int) -> dict:
        url = (
            self.BASE_URL
            + _Endpoints.ISSUES.format(board_id=board_id)
            + f"?startAt={start_at}"
        )
        return self._get(url)
