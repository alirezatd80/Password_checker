def check_length(password):
    length = len(password)
    if length < 7 :
        raise Exception('your password is short')
    return True