from secrets import toggl_token
from services.toggl import Toggl
from stats import ProjectStats, TaskStats, MyDict

SEPARATOR = "\t"


def main():
    toggl = Toggl(api_token=toggl_token)
    start_date = "2023-12-01"
    end_date = "2023-12-09"
    time_entries = toggl.get_time_entries(start_date=start_date, end_date=end_date)

    my_dict = MyDict()

    # project based time
    print(f"Project Stats {'='*50}")
    project_stats = ProjectStats(time_entries, my_dict)
    project_stats.output()

    # task based time
    print(f"Task Stats: {'='*50}")
    task_stats = TaskStats(time_entries, my_dict)
    task_stats.output()


if __name__ == "__main__":
    main()
