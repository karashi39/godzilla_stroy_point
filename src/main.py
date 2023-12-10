# from secrets import toggl_token, jira_token, jira_domain
# from services.toggl import Toggl

# from stats import ProjectStats, TaskStats, MyDict
# from config import PROJECT


def main():
    pass
    # board_id = 5
    # jira = Jira(api_token=jira_token, domain=jira_domain, board_id=board_id)

    # toggl = Toggl(api_token=toggl_token)

    # start_date = "2023-11-01"
    # end_date = "2023-11-30"
    # time_entries = toggl.get_time_entries(start_date=start_date, end_date=end_date)

    # my_dict = MyDict()

    # project based time
    # print(f"Project Stats {'='*45}")
    # project_stats = ProjectStats(time_entries, my_dict)
    # project_stats.output(PROJECT)

    # task based time
    # print(f"Task Stats: {'='*47}")
    # task_stats = TaskStats(time_entries, my_dict)
    # print(f"DEVELOP: {'-'*50}")
    # task_stats.output(PROJECT, "DEVELOP")
    # print(f"MTG: {'-'*54}")
    # task_stats.output(PROJECT, "MTG")


if __name__ == "__main__":
    main()
