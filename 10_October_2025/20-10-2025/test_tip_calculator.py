from Tip_Calculator import calculate_tips


def test_calculator() -> None:
    assert calculate_tips("$10.00", "25%") == ["$1.50", "$2.00", "$2.50"]
    assert calculate_tips("$89.67", "26%") == ["$13.45", "$17.93", "$23.31"]
    assert calculate_tips("$19.85", "9%") == ["$2.98", "$3.97", "$1.79"]
