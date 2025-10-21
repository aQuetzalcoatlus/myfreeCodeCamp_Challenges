"""Thermostat Adjuster 2

Given the current temperature of a room in Fahrenheit and a target temperature in Celsius, return a string indicating how to adjust the room temperature based on these constraints:

    Return "Heat: X degrees Fahrenheit" if the current temperature is below the target. With X being the number of degrees in Fahrenheit to heat the room to reach the target, rounded to 1 decimal place.
    Return "Cool: X degrees Fahrenheit" if the current temperature is above the target. With X being the number of degrees in Fahrenheit to cool the room to reach the target, rounded to 1 decimal place.
    Return "Hold" if the current temperature is equal to the target.

To convert Celsius to Fahrenheit, multiply the Celsius temperature by 1.8 and add 32 to the result (F = (C * 1.8) + 32).
"""


def to_fahrenheit(temp_celsius: float) -> float:
    return temp_celsius * 1.8 + 32


def adjust_thermostat(current_f: float, target_c: float) -> str:
    target_f: float = to_fahrenheit(target_c)
    temp_difference: float = round(current_f - target_f, 1)

    if temp_difference < 0:
        return f"Heat: {abs(temp_difference)} degrees Fahrenheit"
    elif temp_difference > 0:
        return f"Cool: {abs(temp_difference)} degrees Fahrenheit"

    return "Hold"


if __name__ == "__main__":
    print(adjust_thermostat(32, 0))
