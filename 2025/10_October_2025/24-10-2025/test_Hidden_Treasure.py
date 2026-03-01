from Hidden_Treasure import dive


def test_dive() -> None:
    assert dive([["-", "X"], ["-", "X"], ["-", "O"]], [2, 1]) == "Recovered"
    assert dive([["-", "X"], ["-", "X"], ["-", "O"]], [2, 0]) == "Empty"
    assert dive([["-", "X"], ["-", "O"], ["-", "O"]], [1, 1]) == "Found"
    assert dive([["-", "-", "-"], ["X", "O", "X"], ["-", "-", "-"]], [1, 2]) == "Found"
    assert (
        dive([["-", "-", "-"], ["-", "-", "-"], ["O", "X", "X"]], [2, 0]) == "Recovered"
    )
    assert dive([["-", "-", "-"], ["-", "-", "-"], ["O", "X", "X"]], [1, 2]) == "Empty"
