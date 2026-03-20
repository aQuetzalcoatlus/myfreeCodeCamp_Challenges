from Equinox_Shadows import get_shadow


def test_get_shadow() -> None:
    assert get_shadow("10:00") == "8ft west"
    assert get_shadow("15:00") == "27ft east"
    assert get_shadow("12:00") == "No shadow"
    assert get_shadow("17:30") == "166.375ft east"
    assert get_shadow("05:00") == "No shadow"
    assert get_shadow("06:00") == "216ft west"
    assert get_shadow("18:00") == "No shadow"
    assert get_shadow("07:30") == "91.125ft west"
    assert get_shadow("00:00") == "No shadow"
