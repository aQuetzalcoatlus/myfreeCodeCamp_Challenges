from Longest_Word import get_longest_word


def test_get_longest_word() -> None:
    assert get_longest_word("coding is fun") == "coding"
    assert (
        get_longest_word("Coding challenges are fun and educational.") == "educational"
    )
    assert get_longest_word("This sentence has multiple long words.") == "sentence"
