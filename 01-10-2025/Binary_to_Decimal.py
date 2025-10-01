"""
Binary to Decimal

Given a string representing a binary number, return its decimal equivalent as a number.

A binary number uses only the digits 0 and 1 to represent any number. To convert binary to decimal, multiply each digit by a power of 2 and add them together. Start by multiplying the rightmost digit by 2^0, the next digit to the left by 2^1, and so on. Once all digits have been multiplied by a power of 2, add the result together.

"""


def to_decimal(binary: str) -> int:
    number_decimal: int = 0
    for i, bit in enumerate(binary[::-1]):
        number_decimal += (2**i) * int(bit)

    return number_decimal


if __name__ == "__main__":
    print(to_decimal("1010"))
