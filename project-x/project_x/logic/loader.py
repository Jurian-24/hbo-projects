from time import sleep
import os

def progressBar(percent = 0, width = 40):
    left = width * percent // 100
    right = width - left

    tags = '🦦' * left
    spaces = '🥚' * right
    percents = f'{percent:.0f}%'

    print('\r[', tags, spaces, ']', percents, sep = '', end = '', flush = True)

def showProgressBar(gameLoader):
    gameLoader = True

    while gameLoader:
        for i in range(101):
            progressBar(i)
            sleep(0.05)

        gameLoaderCheck = True
        os.system('cls' if os.name == 'nt' else 'clear')

        if gameLoaderCheck == False:
            print('\nError, trying again!')
            continue
        else:
            gameLoader = False

showProgressBar(True)