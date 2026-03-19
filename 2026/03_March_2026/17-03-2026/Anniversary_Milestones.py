"""
Anniversary Milestones
Given an integer representing the number of years a couple has been married, return their most recent anniversary milestone according to this chart:

Years Married	Milestone
1	"Paper"
5	"Wood"
10	"Tin"
25	"Silver"
40	"Ruby"
50	"Gold"
60	"Diamond"
70	"Platinum"
If they haven't reached the first milestone, return "Newlyweds".
"""


def get_milestone(years: float) -> str:
    years_rounded: int = int(years)
    milestones: dict = {
        1: "Paper",
        5: "Wood",
        10: "Tin",
        25: "Silver",
        40: "Ruby",
        50: "Gold",
        60: "Diamond",
        70: "Platinum",
    }

    result: str = "Newlyweds"

    for year, milestone in milestones.items():
        if years_rounded >= year:
            result = milestone

    return result


print(get_milestone(8))
