from word_frequency import get_words

def test_get_words():
    assert get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding") == ["coding", "python", "in"]
    assert get_words("I like coding. I like testing. I love debugging!") == ["i", "like", "coding"]
    assert get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!") == ["debug", "test", "deploy"]