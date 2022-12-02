from matplotlib import pyplot as plt
import requests
import json


def getCoins() -> dict:
    response = requests.get('https://api.basecampcrypto.nl/v1/coin?key=qx95gdbja26sZa5P')

    return json.loads(response.text)


def getCoinInfo(symbol) -> dict:
    response = requests.get(f'https://api.basecampcrypto.nl/v1/coin/{symbol}/history?key=qx95gdbja26sZa5P')

    return json.loads(response.text)

def showGraph(coin, graphChoice):
    coin = getCoinInfo(coin['symbol'])

    dev_x = [day['day'] for day in coin['history']]

    values = [day['value'] for day in coin['history']]


    if graphChoice == 'line':
        plt.plot(dev_x, values)
        plt.xlabel('Day number')
        plt.ylabel(f'Value')
        plt.title(f'Value of {coin["symbol"]} per day')
        plt.show()
    elif graphChoice == 'boxplot':
        fig = plt.figure(figsize =(10, 7))

        plt.boxplot(values)

        plt.show()
    elif graphChoice == 'histogram':
        import numpy

        x = values
        y = numpy.random.normal(150, 40, 100) / x

        plt.scatter(x, y)
        plt.show()


def startApp():
    coins = getCoins()
    choices = []

    for index, coin in enumerate(coins):
        choices.append(f'[{index}] Show {coin["symbol"]}')

    for choice in choices:
        print(choice)

    userChoice = int(input('What do you want to do? '))
    graphChoice = input('Enter the type of graph of you want to see: ')

    graphOfCoin = showGraph(coins[userChoice], graphChoice)

if __name__ == '__main__':

    startApp()
