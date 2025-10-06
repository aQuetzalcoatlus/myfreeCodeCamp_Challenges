from Space_Week_Day_3_Phone_Home import send_message


def test_send_message() -> None:
    assert send_message([300000, 300000]) == 2.5
    assert send_message([384400, 384400]) == 3.0627
    assert send_message([54600000, 54600000]) == 364.5
    assert send_message([1000000, 500000000, 1000000]) == 1674.3333
    assert send_message([10000, 21339, 50000, 31243, 10000]) == 2.4086
    assert send_message([802101, 725994, 112808, 3625770, 481239]) == 21.1597
