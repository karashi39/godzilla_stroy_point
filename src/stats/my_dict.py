from services.toggl import Toggl
from secrets import toggl_token


class MyDict:
    def __init__(self) -> None:
        toggl = Toggl(api_token=toggl_token)
        me = toggl.get_me()
        workspace_id = me.get("default_workspace_id")
        projects = toggl.get_workspace_projects(workspace_id)

        self.my_dict = {
            "user_id": me.get("id"),
            "projects": {p.get("id"): p.get("name") for p in projects},
        }

    def get_user_id(self) -> int:
        return self.my_dict.get("user_id")

    def output_projects(self) -> None:
        print(self.my_dict.get("projects"))

    def get_project_name(self, project_id: int) -> str:
        return self.my_dict["projects"].get(project_id)

    def get_project_id(self, project_name: str) -> int | None:
        if project_name not in self.my_dict["projects"].values():
            return None
        for project_id, value in self.my_dict["projects"].items():
            if project_name == value:
                return project_id
