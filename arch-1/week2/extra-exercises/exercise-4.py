# Problem 4-4: conditional sum

# Ask the user to input three numbers A, B and C. Find out the sum of all the even numbers.
# (e.g. 1, 2, 3 → 2;   2, 3, 4 → 2 + 4 = 6;   2, 8, 10 → 2 + 8 + 10 = 20;   1, 3, 5 → 0)

numberA = int(input('Enter your first number: '))
numberB = int(input('Enter your second number: '))
numberC = int(input('Enter your third number: '))

if(numberA % 2 == 1):
    numberA = 0
if(numberB % 2 == 1):
    numberB = 0
if(numberC % 2 == 1):
    numberC = 0

print(numberA + numberB + numberC)
