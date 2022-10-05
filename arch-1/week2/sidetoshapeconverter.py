"""
Write a program that determines the name of a shape from its number of sides.
Read the number of sides from the user and then report the appropriate name as part of a meaningful message.
Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
If a number of sides outside of this range is entered then your program should display an appropriate error message.
"""

sidesOfShape = int(input())

if(sidesOfShape < 3):
    print('Error: the amount of sides must be at leat 3 with a max of 10 sides')

if(sidesOfShape > 10):
    print('Error: the max amounts of sides is 10. Try again')

if(sidesOfShape == 3):
    print('Your shape is a triangle')
elif(sidesOfShape == 4):
    print('Your shape is a square')
elif(sidesOfShape == 5):
    print('Your shape is a pentagon')
elif(sidesOfShape == 6):
    print('Your shape is a hexagon')
elif(sidesOfShape == 7):
    print('Your shape is a heptagon')
elif(sidesOfShape == 8):
    print('Your shape is a octagon')
elif(sidesOfShape == 9):
    print('Your shape is a nonagon')
elif(sidesOfShape == 10):
    print('Your shape is a decagon')
