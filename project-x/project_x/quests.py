play = True
lifes = 3

if play:
# puzzel 1 Amaru
    print('Quest 1')
    amaruPuzzelCheck = True

    while amaruPuzzelCheck:
        amaruPuzzel = int(input('what is 9 * 3 + 5 = '))

        if amaruPuzzel == 32:
            amaruPuzzelCheck = False
        else:
            if lifes <= 1:
                print('You died.')
                break
            else:
                lifes -= 1

                print('Wrong anser, try again!')
                print(f'{lifes} left.')
                continue

# puzzel 2 Rhino’s ravine
    print('Quest 2')
    rhinosRavineCheck = True

    while rhinosRavineCheck:
        rhinosRavinePuzzel = int(input('What is 9 / 2 * 4 = '))

        if rhinosRavinePuzzel == 18:
            rhinosRavineCheck = False
        else:
            if lifes <= 1:
                print('You died.')
                break
            else:
                lifes -= 1

                print('Wrong anser, try again!')
                print(f'{lifes} left.')
                continue

# puzzel 3 Riverlands
    print('Quest 3')
    riverlandsCheck = True

    while riverlandsCheck:
        riverlandsPuzzel = int(input('What is 180 - (9 ^ 6) = '))

        if riverlandsPuzzel == -531261:
            riverlandsCheck = False
        else:
            if lifes <= 1:
                print('You died.')
                break
            else:
                lifes -= 1

                print('Wrong anser, try again!')
                print(f'{lifes} left.')
                continue

# puzzel 4 The Windhagen
    print('Quest 4')
    theWindhagenCheck = True

    while theWindhagenCheck:
        theWindhagenPuzzel = input('What is the name of the Island where we are located? ').replace(' ', '')

        if theWindhagenPuzzel.upper() == 'THERAIR':
            theWindhagenCheck = False
        else:
            if lifes <= 1:
                print('You died.')
                break
            else:
                lifes -= 1

                print('Wrong anser, try again!')
                print(f'{lifes} left.')
                continue

# puzzel 5 Sodderlands
    print('Quest 5')
    sodderlandsCheck = True

    while sodderlandsCheck:
        sodderlandsPuzzel = input('Who is your king? ').replace(' ', '')

        if sodderlandsPuzzel.upper() == 'JUDISANDRIS':
            sodderlandsCheck = False
        else:
            if lifes <= 1:
                print('You died.')
                break
            else:
                lifes -= 1

                print('Wrong anser, try again!')
                print(f'{lifes} left.')
                continue
