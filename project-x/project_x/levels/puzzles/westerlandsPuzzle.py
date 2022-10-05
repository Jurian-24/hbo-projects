import os

play = True
lifes = int(os.environ.get("LIVES"))

riverlandsCheck = True

while riverlandsCheck:
    riverlandsPuzzel = int(input('What is 180 - (9 ^ 6) = '))

    if riverlandsPuzzel == -531261:
        riverlandsCheck = False

        from ..dialogue.windhagen import *
    else:
        if lifes <= 1:
            print('You died.')
            break
        else:
            lifes -= 1

            print('Wrong anser, try again!')
            print(f'{lifes} left.')
            continue
