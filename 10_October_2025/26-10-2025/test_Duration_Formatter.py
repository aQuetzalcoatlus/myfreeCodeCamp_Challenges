from Duration_Formatter import format


def test_formatter() -> None:
    assert format(500) == "8:20"
    assert format(4000) == "1:06:40"
    assert format(1) == "0:01"
    assert format(5555) == "1:32:35"
    assert format(99999) == "27:46:39"
