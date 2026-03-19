from Anniversary_Milestones import get_milestone


def test_get_milestone():
    assert get_milestone(0) == "Newlyweds"
    assert get_milestone(1) == "Paper"
    assert get_milestone(8) == "Wood"
    assert get_milestone(10) == "Tin"
    assert get_milestone(26) == "Silver"
    assert get_milestone(45) == "Ruby"
    assert get_milestone(50) == "Gold"
    assert get_milestone(64) == "Diamond"
    assert get_milestone(71) == "Platinum"
