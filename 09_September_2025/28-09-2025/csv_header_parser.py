"""
CSV Header Parser

Given the first line of a comma-separated values (CSV) file, return an array containing the headings.

    - The first line of a CSV file contains headings separated by commas.
    - Remove any leading or trailing whitespace from each heading.

"""


def get_headings(csv: str) -> list[str]:
    csv_separated: list[str] = csv.split(",")
    csv_clean: list[str] = [s.lstrip().rstrip() for s in csv_separated]
    return csv_clean


if __name__ == "__main__":
    get_headings("username , email , signup date ")
