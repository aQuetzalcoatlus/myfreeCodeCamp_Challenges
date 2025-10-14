from time_24_to_12 import to_12


def test_converter() -> None:
    assert to_12("1124") == "11:24 AM"
    assert to_12("0900") == "9:00 AM"
    assert to_12("1455") == "2:55 PM"
    assert to_12("2346") == "11:46 PM"
    assert to_12("0030") == "12:30 AM"
