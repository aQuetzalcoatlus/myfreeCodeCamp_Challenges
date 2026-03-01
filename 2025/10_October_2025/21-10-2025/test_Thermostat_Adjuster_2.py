from Thermostat_Adjuster_2 import adjust_thermostat


def test_adjust_thermostat() -> None:
    assert adjust_thermostat(32, 0) == "Hold"
    assert adjust_thermostat(70, 25) == "Heat: 7.0 degrees Fahrenheit"
    assert adjust_thermostat(72, 18) == "Cool: 7.6 degrees Fahrenheit"
    assert adjust_thermostat(212, 100) == "Hold"
    assert adjust_thermostat(59, 22) == "Heat: 12.6 degrees Fahrenheit"
