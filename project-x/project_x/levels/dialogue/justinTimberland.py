import json
import os
from time import sleep

# Clear the console before dialogue
os.system('cls' if os.name == 'nt' else 'clear')

def getFileName(fileName):
    fileName = os.path.splitext(fileName)[0]

    return fileName

with open('data/dialogue.json') as f:
    data = json.load(f)

fileName = getFileName(os.path.basename(__file__))
questions = data['npc'][fileName]['questions']
wrongAnswer = False
givenAnswers = []
availableAnswers = []

for index, i in enumerate(range(len(questions))):
    givenAnswers.clear()

    if wrongAnswer == True:
        i -=  1
        index -= 1

    print(questions[i]['question'])

    for j in range(len(questions[i]['answers'])):
        print(questions[i]['answers'][j])

    while True:
        userAnswer = input('Your answer: ').replace(' ', '')

        if userAnswer not in givenAnswers:
            break;
        else:
            print('You can`t give the same answer')
        if userAnswer in availableAnswers:
            print(f'{userAnswer} isn`t an option. You can only enter the options given before the answers.')
            break;

    givenAnswers.append(userAnswer)

    if questions[i]['question'] == 'No body visits me! Who are you?':
        # If the player chooses to be hostile you will kill the insane within the first question
        if userAnswer.upper() == 'B':
            print(data['npc'][fileName]['finalMessage'])
            print(os.environ.get('PLAYER_NAME') + ' kills Justin Timberland')
            os.environ['ATTACK_STRENGTH'] = str(int(os.environ.get('ATTACK_STRENGTH')) + 7)

            print(f'You earned 7 strength points! Your total strength is now {os.environ.get("ATTACK_STRENGTH")}')
            print('Your path continues...')
            sleep(2)

            from ..puzzles.westerlandsPuzzle import *
        else:
            continue

    if questions[i]['question'] == '[player_name]? Never heard of him, who are you really?!':
        if userAnswer.upper() == 'B':
            print(data['npc'][fileName]['finalMessage'])
            print(os.environ.get('PLAYER_NAME') + ' kills Justin Timberland')
            os.environ['ATTACK_STRENGTH'] = str(int(os.environ.get('ATTACK_STRENGTH')) + 5)

            print(f'You earned 5 strength points! Your total strength is now {os.environ.get("ATTACK_STRENGTH")}')
            print('Your path continues...')
            sleep(2)

            from ..puzzles.westerlandsPuzzle import *
        else:
            continue

    if questions[i]['question'] == 'You are lying! Nobody lies to me!':
        if userAnswer.upper() == 'A':
            print(data['npc'][fileName]['finalMessage'])
            print(os.environ.get('PLAYER_NAME') + ' kills Justin Timberland')
            os.environ['ATTACK_STRENGTH'] = str(int(os.environ.get('ATTACK_STRENGTH')) + 3)

            print(f'You earned 3 strength points! Your total strength is now {os.environ.get("ATTACK_STRENGTH")}')
            print('Your path continues...')
            sleep(2)

            from ..puzzles.westerlandsPuzzle import *


# from .justinTimberland import *
