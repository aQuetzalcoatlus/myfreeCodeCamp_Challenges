from Battle_of_Words import battle


def test_battle() -> None:
    assert battle("hello world", "hello word") == "We win"
    assert battle("Hello world", "hello world") == "We win"
    assert battle("lorem ipsum", "kitty ipsum") == "We lose"
    assert battle("hello world", "world hello") == "Draw"
    assert battle("git checkout", "git switch") == "We win"
    assert battle("Cheeseburger with fries", "Cheeseburger with Fries") == "We lose"
    assert battle("We must never surrender", "Our team must win") == "Draw"
