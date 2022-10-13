def passwordCheck():
    upper_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lower_set = set("abcdefghijklmnopqrstuvwxyz")
    digit_set = {"1234567890"}
    symbol_set = set("*@!?")

    tries = 0

    while tries < 3:
        password = input('')
        password = password.replace(' ', '')

        pass_set = set(password)
        flag = 0

        if 8 <= len(password) <= 20:
            if bool(upper_set.intersection(pass_set)):
                if bool(lower_set.intersection(pass_set)):
                    if bool(digit_set.intersection(pass_set)):
                        if bool(symbol_set.intersection(pass_set)):
                            flag = 1
            if flag:
                return 'Valid'
            else:
                tries += 1
                print('Invalid')
        else:
            tries += 1

        if tries == 3:
            return 'Invalid'

if __name__ == '__main__':
    print(passwordCheck())
