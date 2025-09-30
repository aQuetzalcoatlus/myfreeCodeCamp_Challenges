"""
Phone Number Formatter

Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
"""


def format_number(number: str) -> str:
    formatted_number: str = ""
    number_length: int = len(number)

    if number_length == 11:
        country_code: str = number[0]
        main_number: str = number[1:]
    elif number_length == 12:
        country_code: str = number[0:2]
        main_number: str = number[2:]

    formatted_number += "+" + country_code + " "

    formatted_number += (
        "(" + main_number[:3] + ") " + main_number[3:6] + "-" + main_number[6:]
    )

    return formatted_number


if __name__ == "__main__":
    print(format_number("495552340182"))
