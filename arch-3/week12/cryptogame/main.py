import requests
import json
import time
from dotenv import load_dotenv

# import algorithms

from logic.algorithms.highRisk import highRisk


def getCoins() -> dict:
    response = requests.get('https://api.basecampcrypto.nl/v1/coin?key=qx95gdbja26sZa5P')

    return json.loads(response.text)

def getCoinInfo(symbol) -> dict:
    response = requests.get(f'https://api.basecampcrypto.nl/v1/coin/{symbol}/history?key=qx95gdbja26sZa5P')

    return json.loads(response.text)

if __name__ == '__main__':
    while True:
        time.sleep(1)
        print(highRisk.test())

