"""
Write a function named "generate_random_password" that generates a random password.
The password should have a random length of between 7 and 10 characters.
Each character should be randomly selected from positions 33 to 126 in the ASCII table.
Your function will not take any parameters. It will return the randomly generated password as its only result.

Display the randomly generated password in your file’s main program. Note: Check how Python can choose random elements of a list or string.
"""

import random

def generate_random_password():

    charachters = random.randint(7, 10)
    password = ''

    for char in range(charachters):
        asciiNumber = random.randint(33, 126)

        password += chr(asciiNumber)

    return password


if __name__ == '__main__':
    print(generate_random_password())
