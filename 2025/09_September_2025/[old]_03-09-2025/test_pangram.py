from Pangram import is_pangram


def test_is_pangram() -> None:
    assert is_pangram("hello", "helo")
    assert not is_pangram("hello", "hel")
    assert not is_pangram("hello", "helow")
    assert is_pangram("hello world", "helowrd")
    assert is_pangram("Hello World!", "helowrd")
    assert not is_pangram("Hello World!", "heliowrd")
    assert not is_pangram("freeCodeCamp", "frcdmp")
    assert is_pangram(
        "The quick brown fox jumps over the lazy dog.", "abcdefghijklmnopqrstuvwxyz"
    )
