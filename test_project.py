import pytest
import password_checker


def test_checklength():
    assert password_checker.check_length('12345678') == True
    with pytest.raises(Exception):
        password_checker.check_length('')
        password_checker.check_length('121d')


def test_litter():
    assert password_checker.check_litter('alidsa333e') == False
    assert password_checker.check_litter('asdasdmSssa') == True
    assert password_checker.check_litter('12314353453') == False
    
def test_digit():
    assert password_checker.check_number('sxqwe1213')==True
    assert password_checker.check_number('asfadsfadsf') == False
    assert password_checker.check_number('123123123') == True
    