"""HSL Validator
Given a string, determine whether it is a valid CSS hsl() color value.

A valid HSL value must be in the format "hsl(h, s%, l%)", where:

- h (hue) must be a number between 0 and 360 (inclusive).
- s (saturation) must be a percentage between 0% and 100%.
- l (lightness) must be a percentage between 0% and 100%.

Spaces are only allowed:

- After the opening parenthesis
- Before and/or after the commas
- Before and/or after closing parenthesis
- Optionally, the value can end with a semi-colon (";").

For example, "hsl(240, 50%, 50%)" is a valid HSL value."""

import re

HSL_RE = re.compile(
    r"""^
    hsl                     # literal
    \(
    \s*                     # optional space after '('
    (?:                     # HUE: either integer or float but within 0-360 handled later
    (?P<h>\d+(?:\.\d+)?)  
    )
    \s*,\s*                 # comma with optional surrounding spaces
    (?P<s>\d+(?:\.\d+)?)%   # SATURATION number followed by %
    \s*,\s*
    (?P<l>\d+(?:\.\d+)?)%   # LIGHTNESS number followed by %
    \s*                     # optional space before ')'
    \)
    \s*;?                   # optional trailing semicolon and optional space
    $""",
    re.IGNORECASE | re.VERBOSE,
)

def is_valid_hsl(hsl: str) -> bool:
    if hsl[-1] == ";":
        hsl = hsl[:-1]
    clean_hsl_str: str = "".join(hsl.split())
    hsl_str: str = clean_hsl_str[3:]
    hsl_str_list: list[str] = hsl_str[1:-1].split(",")
    hsl_int_list: list[int] = [int(el.strip("%")) for el in hsl_str_list]
    print(hsl_int_list)

    h_val: int = hsl_int_list[0]
    s_val: int = hsl_int_list[1]
    l_val: int = hsl_int_list[2]

    is_h: bool = h_val >= 0 and h_val <= 360
    is_s: bool = s_val >= 0 and s_val <= 100
    is_l: bool = l_val >= 0 and l_val <= 100

    is_hsl: bool = is_h and is_s and is_l

    return is_hsl


if __name__ == "__main__":
    print(is_valid_hsl("hsl(200, 55%, 75)"))
    # is_valid_hsl("hsl(240, 50%, 50%)") should return True
