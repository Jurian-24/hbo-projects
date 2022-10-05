import os

play = True
lifes = int(os.environ.get("LIVES"))

sodderlandsCheck = True

while sodderlandsCheck:
    sodderlandsPuzzel = input('Who is your king? ').replace(' ', '')

    if sodderlandsPuzzel.upper() == 'JUDISANDRIS':
        sodderlandsCheck = False

        from ..dialogue.kingsMountain import *
    else:
        if lifes <= 1:
            print('You died.')
            break
        else:
            lifes -= 1

            print('Wrong anser, try again!')
            print(f'{lifes} left.')
            continue
