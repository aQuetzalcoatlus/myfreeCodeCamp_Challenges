from second_largest import second_largest


def test_second_largest() -> None:
    assert second_largest([1, 2, 3, 4]) == 3
    assert second_largest([20, 139, 94, 67, 31]) == 94
    assert second_largest([2, 3, 4, 6, 6]) == 4
    assert second_largest([10, -17, 55.5, 44, 91, 0]) == 55.5, (
        "second_largest([10, -17, 55.5, 44, 91, 0]) should return 55.5."
    )
    assert second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]) == 0
