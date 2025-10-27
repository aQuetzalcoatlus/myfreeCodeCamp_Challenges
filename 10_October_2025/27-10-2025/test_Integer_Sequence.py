from Integer_Sequence import sequence


def test_sequence() -> None:
    assert sequence(5) == "12345"
    assert sequence(10) == "12345678910"
    assert sequence(1) == "1"
    assert sequence(27) == "123456789101112131415161718192021222324252627"
