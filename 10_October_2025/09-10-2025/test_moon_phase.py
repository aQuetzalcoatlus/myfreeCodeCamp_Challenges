from Space_Week_Day_6_Moon_Phase import moon_phase


def test_moon_phase():
    assert moon_phase("2000-01-12") == "New"
    assert moon_phase("2000-01-13") == "Waxing"
    assert moon_phase("2014-10-15") == "Full"
    assert moon_phase("2012-10-21") == "Waning"
    assert moon_phase("2022-12-14") == "New"
