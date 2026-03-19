"""
Evenly Divisible
Given two integers, determine if you can evenly divide the first one by the second one.
"""


def is_evenly_divisible(a, b) -> bool:
    return True if a % b == 0 else False
