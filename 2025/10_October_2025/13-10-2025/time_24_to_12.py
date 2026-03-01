"""24 to 12

Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".

    The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".

"""


def to_12(time: str) -> str:
    if len(time) != 4 or not time.isdigit():
        raise ValueError("Input must be a 4-digit string in HHMM format.")

    hour_string, minute_string = time[:2], time[2:]

    hour_int: int = int(hour_string)
    minute_int: int = int(minute_string)

    if not (0 <= hour_int <= 23 and 0 <= minute_int <= 59):
        raise ValueError("Invalid time input.")

    am_pm: str = "AM" if hour_int < 12 else "PM"

    hour_12: int = hour_int % 12 or 12  # converts 0 to 12, 13 to 1, etc.

    return f"{hour_12}:{minute_int:02d} {am_pm}"


if __name__ == "__main__":
    print(to_12("0024"))
