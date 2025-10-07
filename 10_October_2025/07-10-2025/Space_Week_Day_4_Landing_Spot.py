"""
Space Week Day 4: Landing Spot

In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:

    - Each spot in the matrix will contain a number from 0-9, inclusive.
    - Any 0 represents a potential landing spot.
    - Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
    - The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
    - Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
    - Return the indices of the safest landing spot. There will always only be one safest spot.

For instance, given:

[
    [1, 0],
    [2, 0]
]

Return [0, 1], the indices for the 0 in the first array.
"""


def is_square(matrix: list[list[int]]) -> bool:
    outer_size: int = len(matrix)
    inner_size: int = len(matrix[0])

    return outer_size == inner_size


def padded_matrix(matrix: list[list[int]]) -> list[list[int]]:
    matrix_size: int = len(matrix)

    # Note: the 0-padding is done as strings only for better visibility of which is a padded-zero v/s a safe-landing spot
    padded: list = [["0"] * (matrix_size + 2)]

    for row in matrix:
        padded.append(["0"] + row + ["0"])

    padded.append(["0"] * (matrix_size + 2))

    return padded


def find_landing_spot(matrix: list[list[int]]) -> list[int]:
    if not is_square(matrix):
        raise ValueError("Matrix is not square")

    matrix_size: int = len(matrix)
    candidate_spots: list = []
    danger_levels: dict = {}

    padded: list[list[int]] = padded_matrix(matrix)
    for i in range(matrix_size):
        for j in range(matrix_size):
            if matrix[i][j] == 0:
                # print(f"Zero found at {[i, j]}")
                candidate_spots.append([i, j])
                danger_levels[(i, j)] = (
                    int(padded[i][j + 1])
                    + int(padded[i + 2][j + 1])
                    + int(padded[i + 1][j])
                    + int(padded[i + 1][j + 2])
                )
    print(danger_levels)

    safest_position: list = list(min(danger_levels, key=danger_levels.get))

    return safest_position


if __name__ == "__main__":
    print(find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]))
