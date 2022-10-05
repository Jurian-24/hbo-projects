"""
In this exercise you will write a function named "is_integer" that determines whether or not the characters in a string represent a valid integer.
When determining if a string represents an integer you should ignore any leading or trailing white space. Once this white space is ignored,
a string represents an integer if its length is at least 1 and it only contains digits, or if its first character is either + or - and
the first character is followed by one or more characters, all of which are digits. Write a main program that reads a string from the user and
reports whether or not it represents an integer.

Extended version: Extend your program with a different function "remove_non_integer" that if the given input string contains mixed digits and some alphabetic characters,
it removes the alphabetic characters and prints the remaining integer.
Example: given -12R0A89s the program will generate -12089. The ersult of +012R0A89s will be 12089
"""

def is_integer(string):
    string = string.replace(' ', '')
    if len(string) >= 1:
        if string[0] == '+' or string[0] == '-':
            string = string.replace(string[0], '')
        if string.isnumeric():
            print('valid')
            print(True)
        else:
            print('invalid')
            print(False)
    else:
        print('invalid')
        print(False)


def remove_non_integer(string):
    string = string.replace(' ', '')
    newString = ''
    startChar = ''

    for char in string:
        if char == '+' or char == '-':
            startChar = char

        if char.isdigit():
            newString += char

    return f'{startChar}{newString.lstrip("0")}'


if __name__ == "__main__":
    string = input('Enter random characters: ')
    is_integer(string)
    remove_non_integer(string)
