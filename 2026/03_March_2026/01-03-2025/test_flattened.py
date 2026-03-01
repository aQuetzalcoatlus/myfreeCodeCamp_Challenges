from flattened import is_flat


def test_flat() -> None:
    is_flat([1, 2, 3, 4]) == True
    is_flat([1, [2, 3], 4]) == False
    is_flat([1, 0, False, True, "a", "b"]) == True
    is_flat(["a", [0], "b", True]) == False
    is_flat([1, [2, [3, [4, [5]]]], 6]) == False
