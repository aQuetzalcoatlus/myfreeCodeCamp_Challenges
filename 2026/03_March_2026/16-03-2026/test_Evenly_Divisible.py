from Evenly_Divisible import is_evenly_divisible


def test_evenly_divisible():
    assert is_evenly_divisible(4, 2) == True
    assert is_evenly_divisible(7, 3) == False
    assert is_evenly_divisible(5, 10) == False
    assert is_evenly_divisible(48, 6) == True
    assert is_evenly_divisible(3186, 9) == True
    assert is_evenly_divisible(4192, 11) == False
