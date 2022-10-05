import json
import os
from time import sleep
import random

#Clear the console before dialogue
os.system('cls' if os.name == 'nt' else 'clear')

clipLinks = [
    'https://clips.twitch.tv/YummyCrunchyClintmullinsJonCarnage-heJGjwYMdmuYUipM',
    'https://clips.twitch.tv/CourteousShinyPassionfruitBleedPurple-AkeXstYcQQ4MwSt2',
    'https://clips.twitch.tv/AltruisticFriendlyKangarooTBCheesePull-o_NU7mZF2D7xC8uE',
    'https://clips.twitch.tv/OilyKawaiiSamosaAllenHuhu-TC4O5BaOriJZoSjb',
    'https://clips.twitch.tv/BlitheRepleteDurianSeemsGood-agVTyv_4C-c2SZjt'
]

def getFileName(fileName):
    fileName = os.path.splitext(fileName)[0]

    return fileName

def getWinner():
    joeyAttackStrength = 20
    playerAttackStrength = os.environ.get('ATTACK_STRENGTH')

    chanceOfWinning = (int(playerAttackStrength) / joeyAttackStrength) * 100

    if chanceOfWinning >= 100:
        return True
    elif random.randint(0, 100) < chanceOfWinning:
        return False

with open('data/dialogue.json') as f:
    data = json.load(f)

fileName = getFileName(os.path.basename(__file__))
questions = data['npc'][fileName]['questions']

print('🧗🏻')
print('You are climbing the mountain for a while now...')
sleep(2)
print('🏔🦦🏔')
print('Oh no it is Joey the Egg protector!')
sleep(2)

for index, i in enumerate(range(len(questions))):

    print(questions[i]['question'])

    for j in range(len(questions[i]['answers'])):
        print(questions[i]['answers'][j])


    if questions[i]['question'] == 'Why do you want my eggs?':
        userAnswer = input('Your answer: ')
        if userAnswer.lower() == 'b':
            print('Yes I am!')
            continue

    if questions[i]['question'] == 'I will not them without a fight!':
        userAnswer = input('Your answer: ')
        if userAnswer.lower() == 'a':
            playerWon = getWinner()

            if playerWon:
                print("🦦 -> 💀")
                sleep(1)
                print('You have taken Joeys eggs!')
                sleep(1)
                print('*CRACK*')
                sleep(2)
                print('The egg has hatched...')
                sleep(2)
                print('Its your reward!')
                print()

                rewardIndex = random.randint(0, len(clipLinks) - 1)
                print(f'{clipLinks[rewardIndex]}')
                exit()
            else:
                print('You died...')
                print('You will have to start again...')
                print(f'Tip: Try other answers in order to increase your strength. Joeys strength is level 20. Yours was only {os.environ.get("ATTACK_STRENGTH")}.')
                exit()
        break
