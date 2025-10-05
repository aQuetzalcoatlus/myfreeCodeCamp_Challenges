"""Space Week Day 2: Exoplanet Search

For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.

    - Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
    - Characters 0-9 correspond to luminosity levels 0-9.
    - Characters A-Z correspond to luminosity levels 10-35.

A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
"""

import string


def decode_single_reading(single_value: str) -> int:
    decoder_dict1: dict = {str(num): int(num) for num in range(10)}
    decoder_dict2: dict = {
        str(alpha): int(10 + i) for i, alpha in enumerate(string.ascii_uppercase)
    }
    full_decoder: dict = decoder_dict1 | decoder_dict2

    return full_decoder[single_value]


def decode_full_readings(readings: str) -> list[int]:
    decoded_readings: list[int] = [
        decode_single_reading(reading) for reading in readings
    ]
    return decoded_readings


def average_reading(readings) -> float:
    return sum(decode_full_readings(readings)) / len(readings)


def num_single_valid_readings(readings, verbose: bool = False) -> int:
    average_reading_value: float = average_reading(readings)

    valid_readings: list = []
    for alpha in readings:
        decoded_reading: int = decode_single_reading(alpha)
        if decoded_reading <= 0.8 * average_reading_value:
            valid_readings.append({alpha: decoded_reading})

    return len(valid_readings)


def has_exoplanet(readings, verbose: bool = False) -> bool:
    valid_luminosity_readings: list[int] = num_single_valid_readings(readings=readings)

    if valid_luminosity_readings >= 1:
        return True
    else:
        return False
