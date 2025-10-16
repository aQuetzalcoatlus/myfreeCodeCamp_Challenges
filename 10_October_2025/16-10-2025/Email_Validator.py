"""Email Validator

Given a string, determine if it is a valid email address using the following constraints:

    - It must contain exactly one @ symbol.
    - The local part (before the @):
        - Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
        - Cannot start or end with a dot.
    - The domain part (after the @):
        - Must contain at least one dot.
        - Must end with a dot followed by at least two letters.
    - Neither the local or domain part can have two dots in a row.
"""

# PERSONAL NOTE: Since I am a beginner to regex patterns, I found this to be a hard challenge.

import re


def validate(email: str) -> bool:
    required_pattern: re.Pattern[str] = re.compile(
        r"^(?!\.)(?!.*\.\.)[\w.-]+(?<!\.)@[A-Za-z0-9!-]+(?:\.[A-Za-z0-9!-]+)*\.[A-Za-z]{2,}$"
    )

    if required_pattern.match(email):
        return True

    return False


if __name__ == "__main__":
    print(validate("kj@test.co"))
