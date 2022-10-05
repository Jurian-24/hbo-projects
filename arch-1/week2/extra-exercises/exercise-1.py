# Problem 4-1: division test

# Read one number from the standard input. Then print “:)” if the number is divisible by 5. Otherwise, print “:(”

number = int(input('Enter your a number: '))

if(number % 5 == 1):
    print(':(')
else:
    print(':)')
