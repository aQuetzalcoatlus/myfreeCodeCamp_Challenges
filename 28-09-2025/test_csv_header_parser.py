from csv_header_parser import get_headings


def test_get_headings():
    assert get_headings("username , email , signup date ") == [
        "username",
        "email",
        "signup date",
    ]
    assert get_headings("name,age,city") == ["name", "age", "city"]
    assert get_headings("first name,last name,phone") == [
        "first name",
        "last name",
        "phone",
    ]
