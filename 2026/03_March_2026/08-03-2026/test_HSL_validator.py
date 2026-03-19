from HSL_Validator import is_valid_hsl


def test_is_valid_hsl() -> None:
    assert is_valid_hsl("hsl(240, 50%, 50%)") == True
    assert is_valid_hsl("hsl( 200 , 50% , 75% )") == True
    assert is_valid_hsl("hsl(99,60%,80%);") == True
    assert is_valid_hsl("hsl(0, 0%, 0%) ;") == True
    assert is_valid_hsl("hsl(  10  ,  20%   ,  30%   )    ;") == True
    assert is_valid_hsl("hsl(361, 50%, 80%)") == False
    assert is_valid_hsl("hsl(300, 101%, 70%)") == False
    assert is_valid_hsl("hsl(200, 55%, 75)") == False
    assert is_valid_hsl("hsl (80, 20%, 10%)") == False
