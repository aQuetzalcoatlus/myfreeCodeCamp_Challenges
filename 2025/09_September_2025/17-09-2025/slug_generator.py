"""
Slug Generator

Given a string, return a URL-friendly version of the string using the following constraints:

    - All letters should be lowercase.
    - All characters that are not letters, numbers, or spaces should be removed.
    - All spaces should be replaced with the URL-encoded space code %20.
    - Consecutive spaces should be replaced with a single %20.
    - The returned string should not have leading or trailing %20.
"""

import re


def work_pattern1(string: str) -> str:
    return string.lower()


def work_pattern2(string: str, matches: re.Match[str]) -> str:
    for match in matches:
        span_list: list[int] = list(match.span())


def generate_slug(string: str) -> str:
    pattern1: re.Pattern[str] = re.compile(r"[A-Z]")
    matches1: re.Iterator[re.Match[str]] = pattern1.finditer(string)

    if matches1:
        string = work_pattern1(string)

    pattern2: re.Pattern[str] = re.compile(r"[^A-Za-z0-9\s]")
    matches2: re.Iterator[re.Match[str]] = pattern2.finditer(string)

    if matches2:
        for match in matches2:
            print(list(match.span()))

    return string


if __name__ == "__main__":
    generate_slug(r"  ?H^3-1*1]0! W[0%R#1]D  ")
