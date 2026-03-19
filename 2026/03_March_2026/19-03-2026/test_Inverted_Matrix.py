from Inverted_Matrix import invert_matrix


def test_invert_matrix():
    assert invert_matrix([["a", "b"], ["a", "a"]]) == [["b", "a"], ["b", "b"]]
    assert invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]) == [
        [0, 1, 0],
        [0, 0, 0],
        [1, 0, 1],
    ]
    assert invert_matrix(
        [
            ["apple", "banana", "banana", "apple"],
            ["banana", "apple", "apple", "banana"],
            ["banana", "banana", "banana", "apple"],
        ]
    ) == [
        ["banana", "apple", "apple", "banana"],
        ["apple", "banana", "banana", "apple"],
        ["apple", "apple", "apple", "banana"],
    ]
    assert invert_matrix(
        [
            [6, 7, 7, 7, 6],
            [7, 6, 7, 6, 7],
            [7, 7, 6, 7, 7],
            [7, 6, 7, 6, 7],
            [6, 7, 7, 7, 6],
        ]
    ) == [
        [7, 6, 6, 6, 7],
        [6, 7, 6, 7, 6],
        [6, 6, 7, 6, 6],
        [6, 7, 6, 7, 6],
        [7, 6, 6, 6, 7],
    ]
    assert invert_matrix(
        [[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]
    ) == [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]]
