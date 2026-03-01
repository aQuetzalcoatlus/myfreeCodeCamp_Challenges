from Space_Week_Day_7_Launch_Fuel import launch_fuel


def test_launch_fuel() -> None:
    assert launch_fuel(50) == 12.4
    assert launch_fuel(500) == 124.8
    assert launch_fuel(243) == 60.7
    assert launch_fuel(11000) == 2749.8
    assert launch_fuel(6214) == 1553.4
