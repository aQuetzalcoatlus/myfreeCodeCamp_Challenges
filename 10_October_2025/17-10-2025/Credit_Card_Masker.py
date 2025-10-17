"""Credit Card Masker

Given a string of credit card numbers, return a masked version of it using the following constraints:

    The string will contain four sets of four digits (0-9), with all sets being separated by a single space, or a single hyphen (-).
    Replace all numbers, except the last four, with an asterisk (*).
    Leave the remaining characters unchanged.

For example, given "4012-8888-8888-1881" return "****-****-****-1881".

Self Note: Another challenge to practice Regex patterns! :-)
"""

import re


def mask(card: str) -> str:
    cc_pattern: re.Pattern[str] = re.compile(
        r"^(\d{4})([-\s])(\d{4})\2(\d{4})\2(\d{4})$"
    )
    matches = cc_pattern.fullmatch(card)

    if matches:
        # print(matches.groups())
        sep = matches.group(2)
        # print(sep)
        last4 = matches.group(5)
        # print(last4)
    else:
        raise ValueError("Card format must be 4-4-4-4 with spaces or dashes only.")

    return (("*" * 4 + sep) * 3) + last4


if __name__ == "__main__":
    print(mask("4012-8888-8888-1881"))
