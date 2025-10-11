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
    """Convert hex string to its corresponding decimal representation.

    The decimal representation of a hex string is obtained by using its place values.

    Parameters
    -----
        hex_string :str
            The number in hexadecimal representation (as a string) to be converted.

    Returns
    -----
        int_val: int)
            The decimal representation of the number.

    """
    if type(hex_string) is not str:
        raise TypeError("The input should be a string")
    hex_individuals: list[str] = [str(i) for i in range(10)] + [
        alpha for alpha in "ABCDEF"
    ]
    hex_decoder_dict: dict = {hexval: i for i, hexval in enumerate(hex_individuals)}

    int_val: int = 0

    for i, char in enumerate(hex_string[::-1]):
        if char not in hex_individuals:
            raise ValueError(
                f"Character '{char}' is not a valid hex character. Valid characters are 0-9 and A-F."
            )
        int_val += (16**i) * hex_decoder_dict[char]

    return int_val


if __name__ == "__main__":
    print(hex_to_decimal("5F"))
