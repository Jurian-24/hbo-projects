import os
from time import sleep
import logic.loader as Loader

def startGame():
    os.system('cls' if os.name == 'nt' else 'clear')

    playCheck = True

    while playCheck:
        wantToPlay = input('Do you want to play (Yes or No)? ').replace(' ', '')

        if wantToPlay.upper() == 'YES' or wantToPlay.upper() == 'NO':
            playCheck = False
        else:
            print('Allowd values are (Yes or No). Try again!')
            continue

    if wantToPlay.upper() == 'YES':
        gameLoader = True

        # Set enviroment variables for the game
        os.environ['LIVES'] = '3'
        os.environ['ATTACK_STRENGTH'] = '5'
        os.environ['MORAL'] = '1'

        Loader.showProgressBar(gameLoader)

        print('Welcome to the game `The quest for Joey\'s egg\'s`.')
        sleep(0.5)

        # Username check
        userNameCheck = True

        while userNameCheck:
            userName = input('Enter a username: ')
            os.environ['PLAYER_NAME'] = userName

            if len(userName) < 2 or len(userName) > 15:
                print('Can not be smaller than two or larger than ten characters. Try again!')
                continue
            else:
                userNameCheck = False

        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(0.8)
        print(
            "After Judis Andris had fled/banished to Emulandia, he moved to the old city: Amaru. \n"
            "This city has been an important city since 7138 BKE (Before Kingdom of Emoelandia) after Judis reformed the city to its former glory he came across ancient papyrus scrolls. \n"
            "These rolls looked like some sort of treasure map. \n"
            "He has decided to send one of his bodyguards out and complete this quest…"
        )
        sleep(5)

startGame()

# Import next level
from levels.puzzles.amaruPuzzle import *
