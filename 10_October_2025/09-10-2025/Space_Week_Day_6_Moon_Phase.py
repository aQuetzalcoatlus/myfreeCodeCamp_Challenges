"""
Space Week Day 6: Moon Phase

For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:

Use a simplified lunar cycle of 28 days, divided into four equal phases:

    - "New": days 1 - 7
    - "Waxing": days 8 - 14
    - "Full": days 15 - 21
    - "Waning": days 22 - 28

After day 28, the cycle repeats with day 1, a new moon.

    Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
    You will not be given any dates before the reference date.
    Return the correct phase as a string.
"""

from datetime import datetime, timedelta


def moon_phase(date_string: str) -> str:
    reference_date: datetime = datetime.strptime("2000-01-06", "%Y-%m-%d")

    this_date: datetime = datetime.strptime(date_string, "%Y-%m-%d")
    difference: timedelta = int((this_date - reference_date).days + 1)

    difference %= 28

    phases: list = [
        (1, 7, "New"),
        (8, 14, "Waxing"),
        (15, 21, "Full"),
        (22, 28, "Waning"),
    ]

    for day_min, day_max, phase in phases:
        if day_min <= difference <= day_max:
            return phase


if __name__ == "__main__":
    print(moon_phase("2012-10-21"))
