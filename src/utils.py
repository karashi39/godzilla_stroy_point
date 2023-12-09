def display_duration(duration: int) -> str:
    sec = duration % 60
    hour = int(duration / 3600)
    min = int((duration - hour * 3600 - sec) / 60)
    return f"{str(hour).rjust(3)}:{min:02}:{sec:02}"
