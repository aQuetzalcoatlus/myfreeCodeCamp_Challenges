from Space_Week_Day_5_Goldilocks_Zone import goldilocks_zone


def test_goldilocks_zone() -> None:
    assert goldilocks_zone(1) == [0.95, 1.37]
    assert goldilocks_zone(0.5) == [0.28, 0.41]
    assert goldilocks_zone(6) == [21.85, 31.51]
    assert goldilocks_zone(3.7) == [9.38, 13.52]
    assert goldilocks_zone(20) == [179.69, 259.13]
