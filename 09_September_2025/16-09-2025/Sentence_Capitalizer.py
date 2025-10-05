"""
Sentence Capitalizer

Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.

    All other characters should be preserved.
    Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).

"""

import re


def capitalize(paragraph: str) -> str:
    """
    Group 1: start of string (^) OR (|) sentence-ending punctuation ([.!?])

    Group 2: spaces/quotes/etc. after punctuation -- i.e., NOT A-Za-z -- 0 or more (*)

    Group 3: the first letter to capitalize
    """

    pattern: re.Pattern[str] = re.compile(r"(^|[.!?]+)([^A-Za-z]*)([A-Za-z])")
    return pattern.sub(
        lambda m: m.group(1)
        + m.group(2)
        + (m.group(3).upper() if m.group(3).isalpha() else m.group(3)),
        paragraph,
    )


if __name__ == "__main__":
    print(capitalize("i did today's coding challenge... it was fun!!"))
