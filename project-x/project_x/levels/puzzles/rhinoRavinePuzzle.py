import os

play = True
lifes = int(os.environ.get("LIVES"))

rhinosRavineCheck = True

while rhinosRavineCheck:
    rhinosRavinePuzzel = int(input('What is 9 / 2 * 4 = '))

    if rhinosRavinePuzzel == 18:
        rhinosRavineCheck = False
        from ..dialogue.justinTimberland import *
    else:
        if lifes <= 1:
            print('You died.')
            break
        else:
            lifes -= 1

            print('Wrong anser, try again!')
            print(f'{lifes} left.')
            continue
