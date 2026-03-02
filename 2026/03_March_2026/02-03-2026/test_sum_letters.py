from sum_letters import sum_letters


def test_sum_letters() -> None:
    assert sum_letters("Hello") == 52
    assert sum_letters("freeCodeCamp") == 94
    assert sum_letters("The quick brown fox jumps over the lazy dog.") == 473
    assert (
        sum_letters(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci."
        )
        == 1681
    )
    assert sum_letters("</404>") == 0
