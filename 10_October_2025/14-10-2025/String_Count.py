"""String Count

Given two strings, determine how many times the second string appears in the first.

    The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.

"""


def count(text: str, parameter: str) -> int:
    pattern_count: int = 0

    text_length: int = len(text)
    parameter_length: int = len(parameter)

    for i in range(text_length - parameter_length + 1):
        if text[i : i + parameter_length] == parameter:
            pattern_count += 1

    return pattern_count


if __name__ == "__main__":
    print(count("101010101010101010101", "101"))
