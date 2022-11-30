import json
import time
import requests
import prettytable

team_data = {"team_name": '',
             "team_id": '',
             "created": False}


def get_team_data(key):
    end_point_url = f"https://api.basecampcrypto.nl/v1/team?key={key}"

    api_get_request = requests.get(url=end_point_url)

    api_response_data = eval(api_get_request.text)

    node_name = api_response_data['name']
    node_cash = api_response_data['cash']
    node_equity = api_response_data['equity']
    team_data["team_name"] = node_name
    team_data["team_id"] = key
    team_data["created"] = True
    return f"Team Data:\n Team name = {node_name}\n Cash = {node_cash} \n equity = {node_equity}"


def get_coins_data(key):
    end_point_url = f"https://api.basecampcrypto.nl/v1/coin?key={key}"

    api_get_request = requests.get(url=end_point_url)

    api_response_data = eval(api_get_request.text)

    return api_response_data

def get_single_coin_data(key, symbol):
    end_point_url = f"https://api.basecampcrypto.nl/v1/coin/{symbol}?key={key}"

    api_get_request = requests.get(url=end_point_url)

    api_response_data = eval(api_get_request.text)
    print(f"Name = {api_response_data['name']}")
    print(f"Symbol = {api_response_data['symbol']}")
    print(f"History = {api_response_data['history']}")
    print("---")

if __name__ == '__main__':
    request = requests.get('https://api.basecampcrypto.nl/')
    while True:
        print("[1] Get Team Data")
        print("[2] Get Coins data")
        print("[3] Get Single Coin data")

        user_input = input("Enter what you want to do: ")
        if user_input == "1":
            node_key = input('Team key: ')
            print(get_team_data(node_key))
            print(team_data)
        elif user_input == "2":
            if team_data["created"] == True:
                get_coins_data(team_data["team_id"])
            else:
                node_key = input('Team key: ')
                get_coins_data(node_key)
        elif user_input == "3":
            node_key = input('Team key: ')
            node_symbol = input('Coin Symbol: ')
            get_single_coin_data(node_key, node_symbol)

        elif user_input == "4":
            quit()
