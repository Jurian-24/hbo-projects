password = input('Enter a password: ')

if(len(password) >= 10):
    numbers = sum(char.isdigit() for char in password)
    if numbers >= 2:
        letters = sum(c.isalpha() for c in password)
        spaces  = sum(c.isspace() for c in password)
        others  = len(password) - numbers - letters - spaces

        if(others >= 1):
            print('goed')
else:
    print('Error')
