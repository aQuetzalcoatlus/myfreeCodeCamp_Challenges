"""P@ssw0rd Str3ngth!

Given a password string, return "weak", "medium", or "strong" based on the strength of the password.

A password is evaluated according to the following rules:

    It is at least 8 characters long.
    It contains both uppercase and lowercase letters.
    It contains at least one number.
    It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.

Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
"""


def check_length(password: str) -> bool:
    return len(password) >= 8


def check_cases(password: str) -> bool:
    return any(char.isupper() for char in password) and any(
        char.islower() for char in password
    )


def check_number(password: str) -> bool:
    return any(char.isdigit() for char in password)


def check_special_chars(password: str) -> bool:
    chars_list: list[str] = ["!", "@", "#", "$", "%", "^", "&", "*"]

    return any(char in chars_list for char in password)


def check_strength(password: str) -> str:
    # strength_levels: list[str] = ["weak", "medium", "strong"]

    all_checks: list[bool] = [
        check_length(password),
        check_cases(password),
        check_number(password),
        check_special_chars(password),
    ]

    num_checks_satisfied: int = all_checks.count(True)

    strengths_dict: dict = {0: "weak", 1: "weak", 2: "medium", 3: "medium", 4: "strong"}

    return strengths_dict[num_checks_satisfied]


if __name__ == "__main__":
    print(check_strength("HelloWorld1!"))
