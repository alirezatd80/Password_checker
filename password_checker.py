def check_length(password):
    length = len(password)
    if length < 7 :
        raise Exception('your password is short')
    return True


def check_litter(password):
    upper_litter = any(char.isupper() for char in password)
    lower_litter = any(char.lower() for char in password)

    if upper_litter and lower_litter :
        return True
    return False

def check_number(password):
    result = any(char.isdigit() for char in password)
    return result

def check_symbol(password):
    symbols = '!@#$%^&*()?'
    result = any(char in symbols for char in password)
    return result


def password_ratead(password):
    password_rating = 30
    if not(check_length(password) and check_litter(password) and check_number(password) and check_symbol(password)):
        raise Exception('your password not good')
    if len(password)>15:
        password_rating+=20
    count_upper = 0 
    for i in password:
        if i.isupper():
            count_upper+=1
    print(count_upper)
    if count_upper>=3:
        password_rating+=20
    count_symbol = 0
    for i in password:
        if check_symbol(i):
            count_symbol+=1
    if count_symbol>1:
        password_rating+=20
    if "_" in password:
        password_rating+=10
    return password_rating


