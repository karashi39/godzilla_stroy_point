from utils import display_duration
from constants import SEP
from . import MyDict
from config import TAGS


class TaskStats:
    def __init__(self, time_entries: dict, my_dict: MyDict) -> None:
        self.my_dict = my_dict
        data = {}
        for entry in time_entries:
            user_id = entry.get("user_id")
            if user_id != self.my_dict.get_user_id():
                continue

            project_id = entry.get("project_id")
            description = entry.get("description")
            duration = entry.get("duration")

            if project_id in data:
                if description in data[project_id]:
                    data[project_id][description] += duration
                else:
                    data[project_id][description] = duration
            else:
                data[project_id] = {description: duration}
        self.data = data

    def output(self, project_name: str = None, tag: str = None) -> None:
        for key, data in self.data.items():
            if project_name:
                project_id = self.my_dict.get_project_id(project_name)
                if key != project_id:
                    continue
            for task, duration in data.items():
                if tag and tag in TAGS:
                    if True not in [task.startswith(prefix) for prefix in TAGS[tag]]:
                        continue
                print(f"{task}{SEP}{display_duration(duration)}")
