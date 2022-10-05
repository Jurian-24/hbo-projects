# Problem 4-2: two digit number

# Read one number from the standard input. Check if it is a two digit number and print “TRUE” if it is, or print “FALSE” if it is not

number = int(input('Enter a number: '))

if(len(number) == 2):
    print('TRUE')
else:
    print('FALSE')
