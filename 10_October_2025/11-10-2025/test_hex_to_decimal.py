from Hex_to_Decimal import hex_to_decimal


def test_hex_to_decimal() -> None:
    assert hex_to_decimal("A") == 10
    assert hex_to_decimal("15") == 21
    assert hex_to_decimal("2E") == 46
    assert hex_to_decimal("FF") == 255
    assert hex_to_decimal("A3F") == 2623
