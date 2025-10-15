"""HTML Tag Stripper

Given a string of HTML code, remove the tags and return the plain text content.

    - The input string will contain only valid HTML.
    - HTML tags may be nested.
    - Remove the tags and any attributes.

For example, '<a href="#">Click here</a>' should return "Click here".
"""


def strip_tags(html: str) -> str:
    out: list = []
    in_tag: bool = False

    for char in html:
        if char == "<":
            in_tag = True
        elif char == ">":
            in_tag = False
        else:
            if not in_tag:
                out.append(char)

    return "".join(out)


if __name__ == "__main__":
    print(strip_tags('<a href="#">Click here</a>'))
