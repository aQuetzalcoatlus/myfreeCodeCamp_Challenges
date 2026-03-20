"""
Equinox Shadows
Today is the equinox, when the sun is directly above the equator and perfectly overhead at noon. Given a time, determine the shadow cast by a 4-foot vertical pole.

The time will be a string in "HH:MM" 24-hour format (for example, "15:00" is 3pm).
You will only be given a time in 30 minute increments.

Rules:

The sun rises at 6am directly "east", and sets at 6pm directly "west".
A shadow always points opposite the sun.
The shadow's length (in feet) is the number of hours away from noon, cubed.
There is no shadow before sunrise (before 6am), after sunset (6pm or later), or at noon.
Return:

If a shadow exists, return "(length)ft (direction)". For example, "8ft west".
Otherwise, return "No shadow".
For example, given "10:00", return "8ft west" because 10am is 2 hours from noon, so 23 = 8 feet, and the shadow points west because the sun is in the east at 10am.
"""

from time import strptime, struct_time


def get_shadow(time_str: str) -> str:
    timedata: struct_time = strptime(time_str, "%H:%M")
    time_float: float = (
        timedata.tm_hour + timedata.tm_min / 60
        if timedata.tm_min != 0
        else int(timedata.tm_hour)
    )
    t_diff: float = time_float - 12  # Flipped so positive = east, negative = west

    if t_diff < -6 or t_diff == 0 or t_diff >= 6:
        return "No shadow"
    else:
        return (
            f"{round(abs(t_diff) ** 3, 3)}ft east"
            if t_diff > 0
            else f"{round(abs(t_diff) ** 3, 3)}ft west"
        )


print(get_shadow("06:00"))
