import os

play = True
lifes = int(os.environ.get("LIVES"))

if play:
# puzzel 1 Amaru
    print('Puzzle 1')
    amaruPuzzelCheck = True

    while amaruPuzzelCheck:
        amaruPuzzel = int(input('what is 9 * 3 + 5 = '))

        if amaruPuzzel == 32:
            amaruPuzzelCheck = False

            from ..dialogue.banditPlopBridge import *
        else:
            if lifes <= 1:
                print('You died.')
                break
            else:
                lifes -= 1

                print('Wrong anser, try again!')
                print(f'{lifes} left.')
                continue
