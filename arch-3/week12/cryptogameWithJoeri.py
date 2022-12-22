import time
import requests
import json

key = 'mxeLG5bypv6PWD54'


# gets team name and total money
def get_team():
    response = requests.get(url=f"https://api.basecampcrypto.nl/v1/team?key={key}")
    team_data = eval(response.text)
    return team_data


# gets daily values for all crypto
def get_day_values():
    value_list = []
    symbol = ['XUA', 'YIL', 'ZOS']
    for crypto in symbol:
        response = requests.get(url=f"https://api.basecampcrypto.nl/v1/coin/{crypto}?key={key}")
        day_value = eval(response.text)
        value_list.append(day_value)
    return value_list


# buys crypto
def buy_coin(symbol, amount):
    node = {"amount": amount}
    response = requests.post(url=f"https://api.basecampcrypto.nl/v1/coin/{symbol}/buy?key={key}", json=node)
    buy_data = eval(response.text)
    return buy_data


# sells crypto
def sell_coin(symbol, amount):
    node = {"quantity": amount}
    response = requests.post(url=f"https://api.basecampcrypto.nl/v1/coin/{symbol}/sell?key={key}", json=node)
    sell_data = eval(response.text)
    return sell_data


# gets how many stocks you have of each crypto
def get_positions():
    response = requests.get(url=f'https://api.basecampcrypto.nl/v1/positions?key={key}')
    stocks = eval(response.text)
    return stocks


# looks at when to buy and sell YIL
def when_to_take_action_yil(daily_data, positions, team):
        if daily_data[1]['value'] >= 1900 and len(positions) != 0 and positions[0]['quantity'] != 0:
            return sell_coin(daily_data[1]['symbol'], (positions[0]['quantity']))
        elif daily_data[1]['value'] <= 1300 and team['cash'] != 0:
            return buy_coin(daily_data[1]['symbol'], team['cash'])
        else:
            return None


# main
if __name__ == '__main__':
    while True:
        print('-' * 150)
        print("TEAM DATA")
        print(get_team())
        print('')
        print("DAILY VALUES")
        for crypto in get_day_values():
            print(crypto)
        print('')
        print("WALLET")
        for crypto in get_positions():
            print(crypto)
        print('')
        print("BUY/SELL DATA")
        print(when_to_take_action_yil(get_day_values(), get_positions(), get_team()))
        print('')
        time.sleep(1)
