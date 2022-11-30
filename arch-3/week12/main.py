import time
import json
import requests
from prettytable import PrettyTable
import numpy as np


def getCoins() -> dict:
    response = requests.get('https://api.basecampcrypto.nl/v1/coin?key=qx95gdbja26sZa5P')

    return json.loads(response.text)


def getCoinInfo(symbol) -> dict:
    response = requests.get(f'https://api.basecampcrypto.nl/v1/coin/{symbol}/history?key=qx95gdbja26sZa5P')

    return json.loads(response.text)


def getMinOrMax(coin, choice) -> float:
    if choice == 'min':
        minPrice = min(coin['history'], key=lambda x:x['value'])

        return round(minPrice['value'], 2)

    elif choice == 'max':
        maxPrice = max(coin['history'], key=lambda x:x['value'])

        return round(maxPrice['value'], 2)

def getAverage(coin) -> float:
    totalPrice = 0.0

    for price in coin['history']:
        totalPrice += price['value']

    return round(totalPrice / float(len(coin['history'])), 2)

def getStandardDeviation(coin):
    values = []

    for data in coin['history']:
        values.append(data['value'])

    return round(np.std(values), 2)


def getQuarterData(coin, quarter: str):
    quarterDays = {
        "1": {
            "firstDay": 1,
            "lastDay": 90,
        },
        "2": {
             "firstDay": 91,
            "lastDay": 181,
        },
        "3": {
             "firstDay": 182,
            "lastDay": 273,
        },
        "4": {
             "firstDay": 274,
            "lastDay": 365,
        }
    }

    firstDay = quarterDays.get(quarter)['firstDay']
    lastDay = quarterDays.get(quarter)['lastDay']
    values = []

    for index in range(firstDay, lastDay):
        values.append(coin['history'][index]['value'])

    return values

def getQuartile(coin, quarter):
    return np.percentile([value['value'] for index, value in enumerate(coin['history'])], quarter)

def getRange(coin):
    lowest = getMinOrMax(coin, 'min')
    highest = getMinOrMax(coin, 'max')

    return round(highest - lowest, 2)

def getUpsOrDowns(coin, up):
    ups = 0
    downs = 0
    lastValue = 0

    for day in coin['history']:
        if day['value'] > lastValue:
            ups += 1
            lastValue = day['value']
        else:
            downs += 1
            lastValue = day['value']

    if up:
        return ups
    else:
        return downs

def getLongestPeriod(coin, way: str):
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

def getIQR(coin):
    q1 = getQuartile(coin, 25)
    q3 = getQuartile(coin, 75)

    iqr = q3 - q1

    return round(iqr, 2)

def showTable():
    coins = getCoins()

    coinDataDict = {}

    for coin in coins:
        coin = getCoinInfo(coin['symbol'])
        minPrice = getMinOrMax(coin, 'min')
        maxPrice = getMinOrMax(coin, 'max')
        avgPrice = getAverage(coin)
        standardDevation = getStandardDeviation(coin)
        median = getQuartile(coin, 50) # second element from percentile is the median
        firstQuarter = getQuartile(coin, 25)
        thirdQuarter = getQuartile(coin, 75)
        rangeOfCoin = getRange(coin)
        interQuartile = getIQR(coin)
        ups = getUpsOrDowns(coin, True)
        downs = getUpsOrDowns(coin, False)
        longestUpPeriod = getLongestPeriod(coin, 'up')
        longestDownPeriod = getLongestPeriod(coin, 'down')

        coinDataDict[coin['name']] = {
            "minPrice": minPrice,
            "maxPrice": maxPrice,
            "avgPrice": avgPrice,
            "standardDevation": standardDevation,
            "median": median,
            "firstQuarter": firstQuarter,
            "thirdQuarter": thirdQuarter,
            "rangeOfCoin": rangeOfCoin,
            "interQuartile": interQuartile,
            "ups": ups,
            "downs": downs,
            "longestUpPeriod": longestUpPeriod,
            "longestDownPeriod": longestDownPeriod
        }

    table = PrettyTable(['', 'AVG', 'MIN', 'MAX', 'SD', 'Q1', 'Q2', 'Q3', 'RNG', 'IQR', 'UPS', 'DOWNS', 'LUP', 'LDOWN'])

    for coin in coinDataDict:
        coinName = coin
        coin = coinDataDict[coin]

        table.add_row([
            coinName,
            coin['avgPrice'],
            coin['minPrice'],
            coin['maxPrice'],
            coin['standardDevation'],
            coin['firstQuarter'],
            coin['median'],
            coin['thirdQuarter'],
            coin['rangeOfCoin'],
            coin['interQuartile'],
            coin['ups'],
            coin['downs'],
            coin['longestUpPeriod'],
            coin['longestDownPeriod']
        ])

    print(table)

if __name__ == '__main__':
    start_time = time.time()
    showTable()
    print("--- %s seconds ---" % (time.time() - start_time))
