import requests
import json
import time
import os
from dotenv import load_dotenv

# import algorithms

from logic.algorithms.HighRisk import HighRisk
from logic.algorithms.lowRisk import LowRisk

# load env file
load_dotenv()

def getCoins(key) -> dict:
    response = requests.get(f'https://api.basecampcrypto.nl/v1/coin?key={key}')

    return json.loads(response.text)

def getCoinInfo(symbol, key) -> dict:
    response = requests.get(f'https://api.basecampcrypto.nl/v1/coin/{symbol}/history?key={key}')

    return json.loads(response.text)

def getTeamInfo(key) -> dict:
    response = requests.get(f'https://api.basecampcrypto.nl/v1/team?key={key}')

    return json.loads(response.text)

def getAssests(key):
    response = requests.get(f'https://api.basecampcrypto.nl/v1/positions?key={key}')

    return json.loads(response.text)

def startApp(team, assets):
    highRiskInvestment = HighRisk(coins).getHighestRiskCoin()
    lowestRiskInvestment = LowRisk(coins).getLowestRiskCoin()


if __name__ == '__main__':
    key = os.getenv('API_KEY')
    team = getTeamInfo(key)
    coins = getCoins(key)
    assets = getAssests(key)

    startApp(team, assets)
