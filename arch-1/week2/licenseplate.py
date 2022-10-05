"""
Consider a valid license plate in The Netherlands (consider only one valid pattern).
Write a program that begins by reading a string of characters from the user.
Then your program should display a message indicating whether the characters are representing a valid license plate.
"""

# Er zijn 3 formats voor een kentekenplaat: 12-ab-11, 1-111-01, 01-111-1
#Om te kijken of de opgegeven kenteken matched met een format moeten we kijken waar een streep zit.
# Bij de eerste format zit de streep voor controle op index 2 & 5
# BIj de tweede format zit de streep op index 2
# bij de laatste format zit de streep op index 6

licensePlate = input('Enter your license plate: ')

if(len(licensePlate) == 8 ):
    if(licensePlate.count('-') == 2):
        if(licensePlate[2] == '-' and licensePlate[5] == '-'):
            print('Valid license plate, Format: 1')
        elif(licensePlate[2] == '-' and licensePlate[6] == '-'):
            print('Valid license plate, Format 2')
        elif(licensePlate[1] == '-' and licensePlate[6] == '-'):
            print('Valid license plate, Format 3')
    else:
        print('Error: Wrong format')
else:
    print('Error: Your license plate has to be 8 characters long')
