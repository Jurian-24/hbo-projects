import requests
import json

class LowRisk:
    def __init__(self):
        self.coins = self.getCoins('sxtjsubXn365105Y')

    def getLowestRiskCoin(self):
        highestGain = 0.0
        highestLoss= 0.0

        # Get the percentage by looping through the coins. The coin with the lowest loss percentage will be chosen as the lowest risk

        # get longest down trend in days
        periods = {}

        for coin in self.coins:
            print(coin)
            periods[coin['symbol']] = {
                "downs": self.getLongestPeriod(coin, 'down'),
                "ups": self.getLongestPeriod(coin, 'up')
            }
        return
        for symbol, value in periods.items():
            print(value)
            # print(symbol, value['ups'] - value['downs'])

        safestCoins = [symbol for symbol, value in periods.items()
            if value['ups'] - value['downs'] > 0
        ]

        # print(safestCoins)

    def getLongestPeriod(self, coin, way: str):
        longestPeriod = 0
        lastValue = 0.0
        daysCounter = 0

        if way == 'up':
            for day in coin['history']:
                if day['value'] > lastValue or day['value'] == lastValue:
                    daysCounter += 1
                else:

                    if longestPeriod > daysCounter:
                        continue
                    else:
                        longestPeriod = daysCounter

                    daysCounter = 0

                lastValue = day['value']

        elif way == 'down':
            for day in coin['history']:
                if day['value'] < lastValue or day['value'] == lastValue:
                    daysCounter += 1
                else:

                    if longestPeriod > daysCounter:
                        continue
                    else:
                        longestPeriod = daysCounter

                    daysCounter = 0

                lastValue = day['value']

        return longestPeriod


    def getCoins(self, key) -> dict:
        response = requests.get(f'https://api.basecampcrypto.nl/v1/coin?key={key}')

        coins = json.loads(response.text)

        return [self.getCoinInfo(coin['symbol'], key) for coin in coins]


    def getCoinInfo(self, symbol, key) -> dict:
        response = requests.get(f'https://api.basecampcrypto.nl/v1/coin/{symbol}/history?key={key}')

        return json.loads(response.text)


lowRisk = LowRisk()

lowRisk.getLowestRiskCoin()
# print(lowRisk.coins)
