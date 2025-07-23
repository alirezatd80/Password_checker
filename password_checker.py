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

print(check_litter('12314353453'))

