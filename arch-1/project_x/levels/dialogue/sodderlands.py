import json
import os

def getFileName(fileName):
    fileName = os.path.splitext(fileName)[0]

    return fileName

with open('data/dialogue.json') as f:
    data = json.load(f)

fileName = getFileName(os.path.basename(__file__))
questions = data['npc'][fileName]['questions']

for index, i in enumerate(range(len(questions))):
    print(questions[i]['question'])

    for j in range(len(questions[i]['answers'])):
        print(questions[i]['answers'][j])

    if questions[i]['question'] == 'Hello good sir how are you doing today!':
        userAnswer = input('Your answer: ').replace(' ', '')

        if userAnswer.upper() == 'A' or 'B':
            continue

    if questions[i]['question'] == 'You look weak. Please take this potion. It will make you feel stronger and you will need it [player]':
        userAnswer = input('Your answer: ').replace(' ', '')

        if userAnswer.upper() == 'A':
            attack_strength = os.environ["ATTACK_STRENGTH"] = str(int(os.environ.get('ATTACK_STRENGTH')) * int(os.environ.get('MORAL')))
            print(f'Your Attack strength is now: {attack_strength}')
            break
        elif userAnswer.upper() == 'B':
            continue

    if questions[i]['question'] == 'I come from a land far west from here. You dont know nothing about the world. Take this potion [player].':
        attack_strength = os.environ["ATTACK_STRENGTH"] = str(int(os.environ.get('ATTACK_STRENGTH')) * int(os.environ.get('MORAL')))
        print(f'Your Attack strength is now: {attack_strength}')
        break

print('Your climbing up the mountain now...')

from ..puzzles.kingsMountainPuzzle import *
