"""
Decimal to Binary

Given a non-negative integer, return its binary representation as a string.

A binary number uses only the digits 0 and 1 to represent any number. To convert a decimal number to binary, repeatedly divide the number by 2 and record the remainder. Repeat until the number is zero. Read the remainders last recorded to first. For example, to convert 12 to binary:

12 ÷ 2 = 6 remainder 0
6 ÷ 2 = 3 remainder 0
3 ÷ 2 = 1 remainder 1
1 ÷ 2 = 0 remainder 1

12 in binary is 1100.
"""


def to_binary(decimal: int) -> str:
    """Given an integer, represent it as a binary string"""

    this_num: int = decimal
    this_num_binary: str = ""

    while this_num >= 1:
        next_num: int = this_num // 2
        print(f"This number: {this_num}, Next number: {next_num}")
        this_num_binary += str(this_num % 2)
        this_num = next_num

    return this_num_binary[::-1]


if __name__ == "__main__":
    print(to_binary(12))
