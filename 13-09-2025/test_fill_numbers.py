from Missing_Numbers import fill_numbers

def test_fill_numbers():
    assert fill_numbers(28, 25) == [26, 27]
    assert fill_numbers(1126, 215) == list(range(216,1126))