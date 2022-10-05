"""
Develop a program that reads a four-digit integer from the user and displays the sum of the digits in the number.
For example, if the user enters 3141 then your program should display 3+1+4+1=9.
"""

number = input()
sumNumbers = 0
sumString = ''

for index, digit in enumerate(number):
    sumNumbers = sumNumbers + int(number[index])

    if(len(number) != index + 1):
        sumString = sumString + str(number[index]) + '+'
    else:
        sumString = sumString + str(number[index]) + '=' + str(sumNumbers)

print(sumString)
