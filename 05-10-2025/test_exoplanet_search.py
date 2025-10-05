from Space_Week_Day_2_Exoplanet_Search import has_exoplanet


def test_exoplanet_checker():
    assert has_exoplanet("665544554") == False
    assert has_exoplanet("FGFFCFFGG") == True
    assert has_exoplanet("MONOPLONOMONPLNOMPNOMP") == False
    assert has_exoplanet("9AB98AB9BC98A") == False
    assert has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") == True
    assert has_exoplanet("FREECODECAMP") == True
