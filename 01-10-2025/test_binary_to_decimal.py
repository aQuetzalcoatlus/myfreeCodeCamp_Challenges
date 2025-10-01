from Binary_to_Decimal import to_decimal


def test_decimal_converter() -> None:
    assert to_decimal("101") == 5
    assert to_decimal("1010") == 10
    assert to_decimal("10010") == 18
    assert to_decimal("1010101") == 85
