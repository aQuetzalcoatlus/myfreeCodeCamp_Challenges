from Email_Validator import validate


def test_validator() -> None:
    assert validate("a@b.cd") == True
    assert validate("hell.-w.rld@example.com") == True
    assert validate(".b@sh.rc") == False
    assert validate("example@test.c0") == False
    assert validate("freecodecamp.org") == False
    assert validate("develop.ment_user@c0D!NG.R.CKS") == True
    assert validate("hello.@wo.rld") == False
    assert validate("hello@world..com") == False
    assert validate("git@commit@push.io") == False
