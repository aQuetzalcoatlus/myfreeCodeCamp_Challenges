from Space_Week_Day_1_Stellar_Classification import classify_star


def test_star_classifier():
    classify_star(5778) == "G"
    classify_star(2400) == "M"
    classify_star(9999) == "A"
    classify_star(3700) == "K"
    classify_star(3699) == "M"
    classify_star(210000) == "O"
    classify_star(6000) == "F"
    classify_star(11432) == "B"
