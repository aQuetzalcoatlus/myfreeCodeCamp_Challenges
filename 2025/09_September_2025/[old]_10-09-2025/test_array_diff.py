from Array_Diff import array_diff

def test_array_diff():
    assert array_diff(["apple", "banana"], ["apple", "banana", "cherry"]) == ["cherry"]
    assert array_diff(["apple", "banana", "cherry"], ["apple", "banana"]) == ["cherry"]
    assert array_diff(["one", "two", "three", "four", "six"], ["one", "three", "eight"]) == ["eight", "four", "six", "two"]
    assert array_diff(["two", "four", "five", "eight"], ["one", "two", "three", "four", "seven", "eight"]) == ["five", "one", "seven", "three"]
    assert array_diff(["I", "like", "freeCodeCamp"], ["I", "like", "rocks"]) == ["freeCodeCamp", "rocks"]