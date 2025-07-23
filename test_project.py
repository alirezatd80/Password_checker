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
    
def test_symbol():
    assert password_checker.check_symbol('adsfadsfwe@') == True
    assert password_checker.check_symbol('??????????') == True
    assert password_checker.check_symbol('!cds2f3232f') == True
    assert password_checker.check_symbol('adsfadsfwe') == False
    
def test_ratin():
    with pytest.raises(Exception):
        password_checker.password_ratead('asdsda')
        password_checker.password_ratead('13488083Alo')
        password_checker.password_ratead('13488083Alo4fr')
        password_checker.password_ratead('13488083?lo4fr')
        
    assert password_checker.password_ratead("13488083Alo?") == 30
    assert password_checker.password_ratead("13488083Alo??") ==50
    assert password_checker.password_ratead("13488083AloER??") ==70
    assert password_checker.password_ratead("13488083Alo??RT1") ==90
    assert password_checker.password_ratead("13488083Al_o??RT1") ==100
    
    
    
    
    