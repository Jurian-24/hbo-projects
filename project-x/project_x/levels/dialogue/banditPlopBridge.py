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

for index, i in enumerate(range(len(questions))):
    givenAnswers.clear()

    if wrongAnswer == True:
        i -=  1
        index -= 1

    if index + 1 == len(questions):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Loading next level...')
        sleep(3)

        from ..puzzles.rhinoRavinePuzzle import *
        break;

    print(questions[i]['question'])

    for j in range(len(questions[i]['answers'])):
        print(questions[i]['answers'][j])

    while True:
        userAnswer = input('Your answer: ').replace(' ', '')

        if userAnswer not in givenAnswers:
            break;

        print('You can`t give the same answer')

    givenAnswers.append(userAnswer)

    # If the user gives the wrong answer remove a live from their total lives
    if questions[i]['question'] == 'What brings you here?' and userAnswer.upper() == 'B' or questions[i]['question'] == 'What brings you here?' and userAnswer.upper() == 'C':

        # Check if the attack strength is above the requirement to pass the level
        if(os.environ.get('ATTACK_STRENGTH') < '5'):
            os.environ['LIVES'] = str(int(os.environ['LIVES']) - 1)
            # Ask the question again
            wrongAnswer = True
            print('You lost a live. TIP: Approach people a little bit nicer...')
        else:
            print('The bandit attacked you! You killed him out of self defence')
            sleep(2)
            print('Loading next level...')
            sleep(3)
            break;
    elif questions[i]['question'] == 'Why are you looking for that?' and userAnswer.upper() == 'B':
       # Check if the attack strength is above the requirement to pass the level
        if(os.environ.get('ATTACK_STRENGTH') < '5'):
            os.environ['LIVES'] = str(int(os.environ['LIVES']) - 1)
            # Ask the question again
            wrongAnswer = True
            print('You lost a live. TIP: Approach people a little bit nicer...')
        else:
            print('The bandit attacked you! You killed him out of self defence')
            sleep(2)
            print('Loading next level...')
            sleep(3)
            break;

sleep(2)
print('Loading next level...')
sleep(3)

from ..puzzles.rhinoRavinePuzzle import *
