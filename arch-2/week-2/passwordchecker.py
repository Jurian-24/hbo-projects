'''
In an application a valid password must be a combination of digits, uppercase and lowercase letters
and only four symbols * @ ! ? .

The length of the password must not be less than 8 characters
and must not be more than 20 characters.
In case the password is not valid, the user can try maximum three times until it is validated.

Implement a Python program that asks the password of the user and checks if it is a valid password.

* Use sets and set operations to solve this problem.
'''

def passwordCheck():
    validSymbols = {'*', '@', '!', '?'}
    tries = 0

    while tries < 3:
        password = input('Enter a password: ')
        password = password.replace(' ', '')

        if 8 <= len(password) <= 20:
            containsDigit = False
            containsUppercase = False
            containsLowercase = False
            containsSymbol = False

            for char in password:
                if char.isdigit():
                    containsDigit = True
                elif char.isalpha():
                    containsUppercase = True
                elif char.islower():
                    containsLowercase = True
                elif char in validSymbols:
                    containsSymbol = True
                else:
                    print('You used wrong characters')
                    tries += 1
                    break
            if containsDigit and containsUppercase and containsLowercase and containsSymbol:
                return 'Good password'
            else:
                print('a valid password must be a combination of digits, uppercase and lowercase letters and one symbol (* @ ! ?)')
        else:
            print('Your password needs to be 8-20 characters')
            tries += 1


if __name__ == '__main__':
    print(passwordCheck())
