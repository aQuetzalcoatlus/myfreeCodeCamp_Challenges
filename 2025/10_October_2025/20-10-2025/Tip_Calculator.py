"""Tip Calculator

Given the price of your meal and a custom tip percent, return an array with three tip values; 15%, 20%, and the custom amount.

    - Prices will be given in the format: "$N.NN".
    - Custom tip percents will be given in this format: "25%".
    - Return amounts in the same "$N.NN" format, rounded to two decimal places.

For example, given a "$10.00" meal price, and a "25%" custom tip value, return ["$1.50", "$2.00", "$2.50"].
"""


def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:
    price = float(meal_price.strip("$"))
    custom = float(custom_tip.strip("%"))

    tip_percents: list[float] = [15, 20, custom]

    return [f"${price * p / 100:.2f}" for p in tip_percents]


if __name__ == "__main__":
    print(calculate_tips("$10.00", "25%"))
