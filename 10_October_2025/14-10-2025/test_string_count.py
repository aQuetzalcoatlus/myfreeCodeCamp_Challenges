from String_Count import count


def test_string_count() -> None:
    assert count("abcdefg", "def") == 1
    assert count("hello", "world") == 0
    assert count("mississippi", "iss") == 2
    assert count("she sells seashells by the seashore", "sh") == 3
    assert count("101010101010101010101", "101") == 10
