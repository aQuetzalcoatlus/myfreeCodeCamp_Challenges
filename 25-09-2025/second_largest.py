def second_largest(numbers_list: list[float]) -> float:
    """
    Given a list of numbers, return the second largest number.

    Input
    ---
        - `numbers_list` (`list[float]`): list of numbers

    Output
    ---
        - `second_largest` (`float`): second-largest number in the list
    """

    return sorted(list(set(numbers_list)))[-2]


if __name__ == "__main__":
    print(second_largest([10, -17, 55.5, 44, 91, 0]))
