"""Hex to Decimal

Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.

Hexadecimal is a number system that uses 16 digits:

    - 0-9 represent values 0 through 9.
    - A-F represent values 10 through 15.

Here's a partial conversion table:
Hexadecimal 	Decimal
0 	0
1 	1
... 	...
9 	9
A 	10
... 	...
F 	15
10 	16
... 	...
9F 	159
A0 	160
... 	...
FF 	255
100 	256

    The string will only contain characters 0-9 and A-F.

"""


def hex_to_decimal(hex_string: str) -> int:
    hex_individuals: list[str] = [str(i) for i in range(10)] + [
        alpha for alpha in "ABCDEF"
    ]
    hex_decoder_dict: dict = {hexval: i for i, hexval in enumerate(hex_individuals)}

    int_val: int = 0

    for i, char in enumerate(hex_string[::-1]):
        int_val += (16**i) * hex_decoder_dict[char]

    return int_val
