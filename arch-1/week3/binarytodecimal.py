"""
Write a program that converts a binary (base 2) number to decimal (base 10).
Your program should begin by reading the binary number from the user as a string.
Then it should compute the equivalent decimal number by processing each digit in the binary number.
Finally, your program should display the equivalent decimal number with an appropriate message.
"""

binaryNumber = input('')

binaryCheck = {'0', '1'}
t = set(binaryNumber)
if binaryCheck == t or t == {'0'} or t == {'1'}:

    base10Number = 0

    for i in range(len(binaryNumber)):
        base10Number = base10Number + (int(binaryNumber[::-1][i]) * (2**i))
    print(f'{base10Number}')
