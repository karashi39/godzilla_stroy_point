from utils import display_duration
from . import MyDict
from constants import SEP


class ProjectStats:
    def __init__(self, time_entries: dict, my_dict: MyDict) -> None:
        self.my_dict = my_dict
        data = {}
        for entry in time_entries:
            user_id = entry.get("user_id")
            if user_id != self.my_dict.get_user_id():
                continue

            project_id = entry.get("project_id")
            duration = entry.get("duration")

            if project_id in data:
                data[project_id] += duration
            else:
                data[project_id] = duration
        self.data = data

    def output(self) -> None:
        for project_id, duration in self.data.items():
            print(
                f"{self.my_dict.get_project_name(project_id)}:{SEP}{display_duration(duration)}"
            )
