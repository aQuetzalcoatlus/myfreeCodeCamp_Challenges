"""Space Week Day 5: Goldilocks Zone

For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.

Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.

To calculate the Goldilocks Zone:

    - Find the luminosity of the star by raising its mass to the power of 3.5.
    - The start of the zone is 0.95 times the square root of its luminosity.
    - The end of the zone is 1.37 times the square root of its luminosity.

    - Return the distances rounded to two decimal places.

For example, given 1 as a mass, return [0.95, 1.37].
"""

from math import sqrt


def luminosity(mass: float) -> float:
    return mass**3.5


def goldilocks_zone(mass: float) -> list[float]:
    sq_lum: float = sqrt(luminosity(mass))

    zone_start: float = round(0.95 * sq_lum, 2)
    zone_end: float = round(1.37 * sq_lum, 2)

    return [zone_start, zone_end]


if __name__ == "__main__":
    print(goldilocks_zone(0.5))
