def passwordCheck():
    upper_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower_set = set("abcdefghijklmnopqrstuvwxyz")
    digit_set = set("1234567890")
    symbol_set = set("*@!?")
    print(upper_set, lower_set, digit_set, symbol_set)

    tries = 0

    while tries < 3:
        password = input('')
        password = password.replace(' ', '')

        containsUpper, containsLower, containsDigit, containsSymbol = False, False, False, False

        if 8 <= len(password) <= 20:
            for char in password:
                char = set(char)

                if bool(upper_set.intersection(char)):
                    containsUpper = True
                elif bool(lower_set.intersection(char)):
                    containsLower = True
                elif bool(digit_set.intersection(char)):
                    containsDigit = True
                elif bool(symbol_set.intersection(char)):
                    containsSymbol = True
                else:
                    containsUpper, containsLower, containsDigit, containsSymbol = False, False, False, False

            if containsUpper and containsLower and containsDigit and containsSymbol:
                return 'Valid'
            else:
                print(containsUpper, containsLower, containsDigit, containsSymbol)
                tries += 1
                print('Invalid')
        else:
            tries += 1

        if tries == 3:
            print('paashaas')
            return 'Invalid'


if __name__ == '__main__':
    print(passwordCheck())
