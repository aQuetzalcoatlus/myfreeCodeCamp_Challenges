from Space_Week_Day_1_Stellar_Classification import classification


def test_star_classifier():
    assert classification(5778) == "G"
    assert classification(2400) == "M"
    assert classification(9999) == "A"
    assert classification(3700) == "K"
    assert classification(3699) == "M"
    assert classification(210000) == "O"
    assert classification(6000) == "F"
    assert classification(11432) == "B"
