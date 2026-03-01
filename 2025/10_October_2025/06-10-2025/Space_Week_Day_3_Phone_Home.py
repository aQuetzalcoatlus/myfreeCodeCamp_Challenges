"""
Space Week Day 3: Phone Home

For day three of Space Week, you are given an array of numbers representing distances (in kilometers) between yourself, satellites, and your home planet in a communication route. Determine how long it will take a message sent through the route to reach its destination planet using the following constraints:

    - The first value in the array is the distance from your location to the first satellite.
    - Each subsequent value, except for the last, is the distance to the next satellite.
    - The last value in the array is the distance from the previous satellite to your home planet.
    - The message travels at 300,000 km/s.
    - Each satellite the message passes through adds a 0.5 second transmission delay.
    - Return a number rounded to 4 decimal places, with trailing zeros removed.
"""


def send_message(route: list[float]) -> float:
    comm_speed: float = 3e5  # km/s
    transmission_delay: float = 0.5  # s

    time_taken: float = 0
    for i, distance in enumerate(route):
        time_taken += distance / comm_speed
        if i != len(route) and i != 0:
            time_taken += transmission_delay

    return round(time_taken, 4)


if __name__ == "__main__":
    print(send_message([384400, 384400]))
