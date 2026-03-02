"""
Given a string, return the sum of its letters.

Letters are A-Z in uppercase or lowercase
Letter values are: "A" = 1, "B" = 2, ..., "Z" = 26
Uppercase and lowercase letters have the same value.
Ignore all non-letter characters.
"""

import string


def sum_letters(s: str) -> int:
    letter_dict_lower: dict = {c: i + 1 for i, c in enumerate(string.ascii_lowercase)}
    letter_dict_upper: dict = {c: i + 1 for i, c in enumerate(string.ascii_uppercase)}
    combined_letters_dict: dict = letter_dict_lower | letter_dict_upper

    sum_val: int = 0
    for c in s:
        if c in combined_letters_dict:
            sum_val += combined_letters_dict[c]
        else:
            sum_val += 0

    return sum_val


print(sum_letters("freeCodeCamp"))
