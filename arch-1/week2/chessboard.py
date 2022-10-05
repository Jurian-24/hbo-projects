"""
Positions on a chess board are identified by a letter and a number.
Usually, the letter identifies the column, while the number identifies the row.
Write a program that reads a position from the user.
The program should determine if the column begins with a black square or a white square.
Then use modular arithmetic (check if you know this concept) to report the color of the square in that row.
For example, if the user enters a1 then your program should report that the square is black.
If the user enters d5 then your program should report that the square is white.
Your program may assume that a valid position will always be entered.
It should report proper error message in case on invalid input values.
"""

# IDEE een odd checker uitvoeren. Bijvoorbeeld a = 1 == odd 1 = odd == black
# Wanneer het eerste getal odd is, is het vakje zwart.

playerPosition = input('Your chess position: ')

if(len(playerPosition) == 2):
    squareRow = playerPosition[0]
    squareNumber = playerPosition[1]

    blackStarter = ['a', 'c', 'e', 'g']
    whiteStarter = ['b', 'd', 'f', 'h']

    if(squareRow in blackStarter):

        indexPlayerPosition = blackStarter.index(squareRow)
        #Convert alphabet to numbers
        blackStarter = ['1', '3', '5', '7']

        square = blackStarter[indexPlayerPosition] + squareNumber

        if(int(square) % 2 == 1):
            print('You are standing on a black square!')
            exit()
        else:
            print('You are standing on a white square!')
            exit()

    if(squareRow in whiteStarter):

        indexPlayerPosition = whiteStarter.index(squareRow)
        #Convert alphabet to numbers
        whiteStarter = ['2', '4', '6', '8']

        square = whiteStarter[indexPlayerPosition] + squareNumber

        if(int(square) % 2 == 1):
            print('You are standing on a white square!')
            exit()
        else:
            print('You are standing on a black square!')
            exit()
else:
    print('Error: Wrong square format, use a1, b5, d4 etc...')
