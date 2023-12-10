from config import SP_FIELD_NAME

from services.jira import Jira as Api


class Jira:
    def __init__(self, api_token: str, domain: str, board_id: int) -> None:
        self.api_token = api_token
        self.domain = domain
        self.board_id = board_id
        self.api = Api(api_token=api_token, domain=domain)
        self._set_issues()

    def _set_issues(self):
        data, total = self._api_get_issues(0)
        self.issues = data
        x = int(total / len(data))
        for i in range(x):
            start_at = len(self.issues) + 1
            data, total = self._api_get_issues(start_at)
            self.issues += data

    def _api_get_issues(self, start_at: int) -> tuple[list, int]:
        data = self.api.get_issues(self.board_id, start_at)
        print(data)
        rows = []
        issues = data.get("issues")
        total = data.get("total")
        for issue in issues:
            fields = issue.get("fields")
            assignee = fields.get("assignee") or {}
            row = {
                "id": issue.get("key"),
                "summary": fields.get("summary"),
                "assignee": assignee.get("displayName"),
                "story_point": fields.get(SP_FIELD_NAME),
            }
            rows.append(row)

        return rows, total
