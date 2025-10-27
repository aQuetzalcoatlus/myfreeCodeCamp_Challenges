"""Integer Sequence

Given a positive integer, return a string with all of the integers from 1 up to, and including, the given number, in numerical order.

For example, given 5, return "12345".
"""


def sequence(n: int) -> str:
    return "".join(str(i + 1) for i in range(n))


if __name__ == "__main__":
    print(sequence(15))
