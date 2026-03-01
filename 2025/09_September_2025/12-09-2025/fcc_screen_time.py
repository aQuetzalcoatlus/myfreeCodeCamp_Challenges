"""
PURE PYTHON:

def too_much_screen_time(days):
    if len(days) != 7:
        raise ValueError(f"Expected 7 values, got {len(days)}")

    # Rule 1: any single day >= 10
    if any(day >= 10 for day in days):
        return True

    # Rule 2: any 3-day sliding average >= 8
    for i in range(len(days) - 2):
        if sum(days[i:i+3]) / 3 >= 8:
            return True

    # Rule 3: 7-day average >= 6
    if sum(days) / 7 >= 6:
        return True

    return False
"""


 # Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

#     If any single day has 10 hours or more, it's too much.
#     If the average of any three days in a row is greater than or equal to 8 hours, it's too much.
#     If the average of the seven days is greater than or equal to 6 hours, it's too much.

import numpy as np

def is_single_day_limit(days_list: list[int]) -> bool:

    if len(days_list) != 7:
        # Fail fast with a clear message instead of continuing in a bad state.
        raise ValueError(f"Expected 7 values, got {len(days_list)}")
    
    days_arr: np.ndarray = np.array(days_list)

    single_day_check = (days_arr >= 10)

    return np.any(single_day_check)

def is_three_day_limit(days_list: list[int]) -> bool:
    if len(days_list) != 7:
        # Fail fast with a clear message instead of continuing in a bad state.
        raise ValueError(f"Expected 7 values, got {len(days_list)}")

    days = np.array(days_list)

    # Vectorized sliding 3-day averages via convolution
    kernel = np.ones(3) / 3
    avg3 = np.convolve(days, kernel, mode='valid')   # shape: (5,)

    # Return a boolean directly (no if/else needed)
    return np.any(avg3 >= 8)

def is_all_week_limit(days_list: list[int]) -> bool:

    if len(days_list) != 7:
        # Fail fast with a clear message instead of continuing in a bad state.
        raise ValueError(f"Expected 7 values, got {len(days_list)}")

    avg_all_week: float = np.mean(days_list)

    return avg_all_week >= 6

def too_much_screen_time(days_list) -> bool:

    if len(days_list) != 7:
        # Fail fast with a clear message instead of continuing in a bad state.
        raise ValueError(f"Expected 7 values, got {len(days_list)}")

    return is_single_day_limit(days_list) or is_three_day_limit(days_list) or is_all_week_limit(days_list)


input_lists = [[1, 2, 3, 4, 5, 6, 7],
                [7, 8, 8, 4, 2, 2, 3],
                [5, 6, 6, 6, 6, 6, 6],
                [1, 2, 3, 11, 1, 3, 4],
                [1, 2, 3, 10, 2, 1, 0],
                [3, 3, 5, 8, 8, 9, 4],
                [3, 9, 4, 8, 5, 7, 6]
]

for input_list in input_lists:
    print(too_much_screen_time(input_list))