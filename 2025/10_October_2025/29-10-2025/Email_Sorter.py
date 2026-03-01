"""Email Sorter

On October 29, 1971, the first email ever was sent, introducing the username@domain format we still use. Now, there are billions of email addresses.

In this challenge, you are given a list of email addresses and need to sort them alphabetically by domain name first (the part after the @), and username second (the part before the @).

    Sorting should be case-insensitive.
    If more than one email has the same domain, sort them by their username.
    Return an array of the sorted addresses.
    Returned addresses should retain their original case.

For example, given ["jill@mail.com", "john@example.com", "jane@example.com"], return ["jane@example.com", "john@example.com", "jill@mail.com"].
"""

import re


def get_domain(email: str) -> str:
    """Given an email address, return the domain name."""
    return email.split("@")[1][:-4]


def sort(emails: list[str]) -> list[str]:
    emails_dict: dict = {email: get_domain(email) for email in emails}
    sorted_emails: dict[str, str] = dict(
        sorted(emails_dict.items(), key=lambda item: item[1])
    )
    print(sorted_emails)
    return list(sorted_emails.keys())
