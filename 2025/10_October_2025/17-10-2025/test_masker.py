from Credit_Card_Masker import mask


def test_mask() -> None:
    assert mask("4012-8888-8888-1881") == "****-****-****-1881"
    assert mask("5105 1051 0510 5100") == "**** **** **** 5100"
    assert mask("6011 1111 1111 1117") == "**** **** **** 1117"
    assert mask("2223-0000-4845-0010") == "****-****-****-0010"
