"""Duration Formatter

Given an integer number of seconds, return a string representing the same duration in the format "H:MM:SS", where "H" is the number of hours, "MM" is the number of minutes, and "SS" is the number of seconds. Return the time using the following rules:

    - Seconds: Should always be two digits.
    - Minutes: Should omit leading zeros when they aren't needed. Use "0" if the duration is less than one minute.
    - Hours: Should be included only if they're greater than zero.

"""


def format(seconds: int) -> str:
    hours: int = seconds // 3600
    mins: int = (seconds // 60) % 60
    seconds_remaining: int = seconds % 60

    if hours and mins:
        return f"{hours}:{mins:0>2}:{seconds_remaining:0>2}"
    elif mins and not hours:
        return f"{mins:0>1}:{seconds_remaining:0>2}"
    return f"0:{seconds_remaining:0>2}"


if __name__ == "__main__":
    print(format(500))  # should return "8:20".
