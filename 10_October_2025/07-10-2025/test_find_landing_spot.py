from Space_Week_Day_4_Landing_Spot import find_landing_spot


def test_find_landing_spot() -> None:
    assert find_landing_spot([[1, 0], [2, 0]]) == [0, 1], "test 1"
    assert find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) == [1, 1], "test 2"
    assert find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) == [2, 2], "test 3"
    assert find_landing_spot(
        [[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]
    ) == [
        2,
        1,
    ], "test 4"
