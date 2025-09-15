from Thermostat_Adjuster import adjust_thermostat

def test_adjust_thermostat():
    assert adjust_thermostat(68, 72) == "heat"
    assert adjust_thermostat(75, 72) == "cool"
    assert adjust_thermostat(72, 72) == "hold"
    assert adjust_thermostat(-20.5, -10.1) == "heat"
    assert adjust_thermostat(100, 99.9) == "cool"
    assert adjust_thermostat(0.0, 0.0) == "hold"
    