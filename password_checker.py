import string
import secrets


def check_length(password):
    length = len(password)
    if length < 7 :
        print('**your password is short**')
        return False
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
        print('**password not good**')
        return 0
    if len(password)>15:
        password_rating+=20
    count_upper = 0 
    for i in password:
        if i.isupper():
            count_upper+=1
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


def generate_password(length=8):
    if length < 8 :
        raise Exception('your password is short')
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digit = string.digits
    symbol = "!@#$%^&*()?"
    allchar = lowercase+uppercase+digit+symbol
    
    password =[
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digit),
        secrets.choice(symbol),
        "_"
    ]
    
    
    for _ in range(length-4):
        password.append(secrets.choice(allchar))
        
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)


def main():
    print('Welcome there') 
    order = 0
    while(order !=3):
        print('1 for checkpassword\n2 for generatepassword\n3 for exit\n')
        order = int((input('your order : ')))
        match(order):
            case 1 :
                password = input('enter your password : ')
                print(password_ratead(password))
            case 2 :
                print(f'*** your password : {generate_password(int(input('enter length : ')))} ***')
            case 3 :
                exit()
            case _ :
                print('number is not correct')
                
if __name__ == "__main__":
    main()
            
                
    
    
    