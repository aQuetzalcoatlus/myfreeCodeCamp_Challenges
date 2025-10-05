from Phone_Number_Formatter import format_number


def test_format_number() -> None:
    assert format_number("05552340182") == "+0 (555) 234-0182"
    assert format_number("15554354792") == "+1 (555) 435-4792"
