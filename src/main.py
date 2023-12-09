from secrets import toggl_token
from services.toggl import Toggl


def main():
    toggl = Toggl(api_token=toggl_token)
    me = toggl.get_me()
    print(me)


if __name__ == "__main__":
    main()
