from Password_Strength import check_strength


def test_password_checker() -> None:
    assert check_strength("123456") == "weak"
    assert check_strength("pass!!!") == "weak"
    assert check_strength("Qwerty") == "weak"
    assert check_strength("PASSWORD") == "weak"
    assert check_strength("PASSWORD!") == "medium"
    assert check_strength("PassWord%^!") == "medium"
    assert check_strength("qwerty12345") == "medium"
    assert check_strength("PASSWORD!") == "medium"
    assert check_strength("PASSWORD!") == "medium"
    assert check_strength("S3cur3P@ssw0rd") == "strong"
    assert check_strength("C0d3&Fun!") == "strong"
