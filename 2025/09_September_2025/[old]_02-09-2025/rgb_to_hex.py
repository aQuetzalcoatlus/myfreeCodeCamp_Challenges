"""
RGB to Hex

Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:
Input 	Output
"rgb(255, 255, 255)" 	"#ffffff"
"rgb(1, 2, 3)" 	"#010203"

    Make any letters lowercase.
    Return a # followed by six characters. Don't use any shorthand values.
"""

def rgb_tuple_to_hex(rgb_tuple: tuple) -> str:
    R, G, B = rgb_tuple
    R_hex, G_hex, B_hex = hex(R)[2:], hex(G)[2:], hex(B)[2:]
    if len(R_hex) == 1:
        R_hex = R_hex.zfill(2)
    if len(G_hex) == 1:
        G_hex = G_hex.zfill(2)
    if len(B_hex) == 1:
        B_hex = B_hex.zfill(2)
    
    hex_str: str = '#'+ R_hex + G_hex + B_hex
    
    return hex_str

def rgb_str_to_tuple(rgb_str: str) -> tuple:
    main_chunk: str = rgb_str[4:-1]
    main_tuple: tuple = main_chunk.split(', ')
    main_tuple_int: tuple[int] = tuple([int(t) for t in main_tuple])

    return main_tuple_int

def rgb_to_hex(rgb_str: str) -> str:
    rgb_tuple: tuple[int] = rgb_str_to_tuple(rgb_str)
    hex_str = rgb_tuple_to_hex(rgb_tuple)

    return hex_str

if __name__=='__main__':
    test_input = "rgb(255, 255, 255)"
    print(rgb_to_hex(test_input))