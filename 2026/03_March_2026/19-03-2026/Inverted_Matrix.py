"""
Inverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
    ["a", "b"],
    ["a", "a"]
]
Return:

[
    ["b", "a"],
    ["b", "b"]
]
"""


def invert_matrix(arr: list[list]) -> list[list]:
    # flatten the array
    arr_flat: list = [item for row in arr for item in row]
    vals_set: list = list(set(arr_flat))

    arr_inverted: list = arr.copy()
    for i, row in enumerate(arr):
        for j, item in enumerate(row):
            if item == vals_set[0]:
                arr_inverted[i][j] = vals_set[1]
            else:
                arr_inverted[i][j] = vals_set[0]

    return arr_inverted


print(invert_matrix([["a", "b"], ["a", "a"]]))
