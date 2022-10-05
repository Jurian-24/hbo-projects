import json
from time import sleep
import os

# Clear the console before dialogue
os.system('cls' if os.name == 'nt' else 'clear')

def getFileName(fileName):
    fileName = os.path.splitext(fileName)[0]

    return fileName

with open('data/dialogue.json') as f:
    data = json.load(f)

fileName = getFileName(os.path.basename(__file__))
questions = data['npc'][fileName]['questions']

# Let the player rest and choose if the user wants to share its campfire

print('It has been a long day. Time for some rest.')
sleep(1)
print('What is that in the bushes...')
sleep(1)
print('🌲⛺️')
sleep(1)
print('🌲🏇🏻⛺️')
sleep(1)
print('It is Tywin Wennister!')
print('May I share your fire with you please? It is very cold!')

shareFire = input('Share fire with Tywin? (Yes or No): ').replace(' ', '')

if shareFire.upper() == 'YES' or shareFire.upper() == 'NO':
    if shareFire.upper() == 'YES':
        os.environ['MORAL'] = str(int(os.environ.get('MORAL')) + 1)
        print('You have earned 1 moral point')

if shareFire.upper() == 'YES' or shareFire.upper() == 'NO':
    if shareFire.upper() == 'YES':
        for index, i in enumerate(range(len(questions))):
            sleep(2)
            # if index + 1 == len(questions):
            #     print('opening new level...')
            #     break
            print()
            print(f'Tywin: {questions[i]["question"]}')
            sleep(2)

            for j in range(len(questions[i]['answers'])):
                print()
                print(f'{os.environ.get("PLAYER_NAME")}: {questions[i]["answers"][j]}')

        print(f'The next morning Tywin Wennister was already gone but he left a note saying: "{data["npc"][fileName]["finalMessage"]}"')
    else:
        print('That is very sad to hear. Have a goodnight...')

print('There are 2 paths. You can either go North and fight Joey the Egg protector or you can choose to go east, take a little detour and explore another location...')

while True:
    direction = input('Which direction do you want to go? (North or East): ').replace(' ', '')

    if direction.upper() == 'NORTH' or direction.upper() == 'EAST':
        if direction.upper() == 'NORTH':
            from .kingsMountain import *
            break;
        elif direction.upper() == 'EAST':
            from ..puzzles.marbensDrop import *
            break;

    print('You can only go North or east')
