import re


def password_validator():
    while True:
        password = input('Enter your password\n')
        if len(password) < 8:
            print('Password should be at least 8 characters long')
        elif not re.search(r'[A-Z]', password):
            print('Password must have at least one uppercase letter')
        elif not re.search(r'[a-z]', password):
            print('Password must have lowercase letters')
        elif not re.search(r'\d', password):
            print('Password must have at least one digit')
        elif not re.search(r'[!@#$%^&*_-]', password):
            print('Password must have at least one special character')
        else:
            return print('This password: ', password, 'is valid!!!')


password_validator()
