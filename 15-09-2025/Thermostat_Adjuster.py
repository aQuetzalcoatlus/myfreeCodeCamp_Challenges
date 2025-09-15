"""
Thermostat Adjuster

Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:

    Return "heat" if the current temperature is below the target.
    Return "cool" if the current temperature is above the target.
    Return "hold" if the current temperature is equal to the target.
"""

def adjust_thermostat(temp: float, target: float) -> str:
    is_cool = temp < target
    is_warm = temp > target
    is_perfect = temp == target

    if is_cool:
        return 'heat'
    elif is_warm:
        return 'cool'
    else:
        return 'hold'

if __name__=='__main__':
    current_temp: float = 23.5
    target_temp: float = 27.1
    print(adjust_thermostat(current_temp, target_temp))