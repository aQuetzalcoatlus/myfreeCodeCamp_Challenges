from Missing_Socks import sock_pairs


def test_sock_pairs() -> None:
    assert sock_pairs(2, 5) == 1
    assert sock_pairs(1, 2) == 0
    assert sock_pairs(5, 11) == 4
    assert sock_pairs(6, 25) == 3
    assert sock_pairs(1, 8) == 0
