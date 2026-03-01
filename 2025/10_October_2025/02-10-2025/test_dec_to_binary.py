from Division_Decimal_to_Binary import to_binary


def test_binary_converter() -> None:
    assert to_binary(5) == "101"
    assert to_binary(12) == "1100"
    assert to_binary(50) == "110010"
    assert to_binary(99) == "1100011"
