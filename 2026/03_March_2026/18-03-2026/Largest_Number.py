"""Largest Number
Given a string of numbers separated by various punctuation, return the largest number.

The given string will only contain numbers and separators.
Separators can be commas (","), exclamation points ("!"), question marks ("?"), colons (":"), or semi-colons (";").
"""

import re


def largest_number(num_str: str) -> float:
    parts: list = re.split("[,!?:;]", num_str)
    return max([float(item) for item in parts])


print(largest_number("4;15:60,26?52!0"))
