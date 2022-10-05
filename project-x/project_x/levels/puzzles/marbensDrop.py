import os

play = True
lifes = int(os.environ.get("LIVES"))

theWindhagenCheck = True

while theWindhagenCheck:
    theWindhagenPuzzel = input('What is the name of the Island where we are located? ').replace(' ', '')

    if theWindhagenPuzzel.upper() == 'THERAIR':
        theWindhagenCheck = False

        from ..dialogue.sodderlands import *
    else:
        if lifes <= 1:
            print('You died.')
            break
        else:
            lifes -= 1

            print('Wrong anser, try again!')
            print(f'{lifes} left.')
            continue
