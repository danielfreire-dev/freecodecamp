def add_time(start: str, duration: str, starting_day: str = None) -> str:
    LIST_OF_DAYS: list[str] = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    time, pm_am = start.split()
    pm_am = pm_am.strip().upper()
    hours, mins = time.strip().split(":")
    
    if starting_day:
        starting_day: str = starting_day.strip().capitalize()
    
    duration_hours, duration_mins = duration.strip().split(":")

    
    duration_hours_int: int = int(duration_hours)
    duration_mins_int: int = int(duration_mins)
    hours_int: int = int(hours)
    mins_int: int = int(mins)

    if duration_mins_int > 59 or duration_mins_int < 0:
        return f"Error: Minutes of the duration are out of bounds: {duration_mins_int}"

    if mins_int > 59 or mins_int < 0:
        return f"Error: Minutes of for the time are out of bounds: {mins_int}"

    if starting_day not in LIST_OF_DAYS and None:
        return f"Error: {starting_day} is no day in a week."

    if pm_am not in ["AM", "PM"]:
        return f"Error: {pm_am} is not a vaild day period."

    if pm_am == "PM":
        hours_int += 12

    combined_time: int = duration_mins_int + mins_int
    combined_hour, combined_mins = divmod(combined_time, 60)

    total_hours: int = duration_hours_int + combined_hour + hours_int
    total_mins: int = combined_mins

    days_passed: int = int(total_hours / 24)

    new_hours: int = total_hours % 24
    new_mins: int = total_mins

    period = "AM"
    if new_hours >= 12:
        new_hours -= 12
        if new_hours == 0:
            new_hours = 12
        period = "PM"

    if new_hours == 0:
        new_hours = 12

    if starting_day is None:
        if days_passed > 1:
            new_time = f"{new_hours}:{new_mins:02d} {period} ({days_passed} days later)"
        elif days_passed == 1:
            new_time = f"{new_hours}:{new_mins:02d} {period} (next day)"
        else:
            new_time = f"{new_hours}:{new_mins:02d} {period}"
    else:
        new_day = LIST_OF_DAYS[
            (LIST_OF_DAYS.index(starting_day) + 1 + days_passed) % 7 - 1
        ]
        if days_passed > 1:
            new_time = f"{new_hours}:{new_mins:02d} {period}, {new_day} ({days_passed} days later)"
        elif days_passed == 1:
            new_time = f"{new_hours}:{new_mins:02d} {period}, {new_day} (next day)"
        else:
            new_time = f"{new_hours}:{new_mins:02d} {period}, {new_day}"

    return new_time