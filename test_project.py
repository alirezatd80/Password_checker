import pytest
import password_checker


def test_checklength():
    assert password_checker.check_length('12345678') == True
    with pytest.raises(Exception):
        password_checker.check_length('')
        password_checker.check_length('121d')
    
    