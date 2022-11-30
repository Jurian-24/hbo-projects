import numpy
import requests
import statistics
from prettytable import PrettyTable

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

    for item in api_response_data:
        print(f"Name = {item['name']}")
        print(f"Symbol = {item['symbol']}")
        print("---")


def get_single_coin_value(key, symbol):
    end_point_url = f"https://api.basecampcrypto.nl/v1/coin/{symbol}?key={key}"

    api_get_request = requests.get(url=end_point_url)

    api_response_data = eval(api_get_request.text)
    print(f"Name = {api_response_data['name']}")
    print(f"Symbol = {api_response_data['symbol']}")
    print(f"Day = {api_response_data['symbol']}")
    print(f"Value = {api_response_data['value']}")


def get_single_coin_value_history(key, symbol):
    coin_value_data = []
    end_point_url = f"https://api.basecampcrypto.nl/v1/coin/{symbol}/history?key={key}"

    api_get_request = requests.get(url=end_point_url)

    api_response_data = eval(api_get_request.text)
    print(f"Name = {api_response_data['name']}")
    print(f"Symbol = {api_response_data['symbol']}")
    print(f"History:")
    for item in api_response_data['history']:
        print(f"Day = {item['day']}")
        print(f"Value = {item['value']}")
        print("-")
        coin_value_data.append(item['value'])
    print("---")

    min_value = min(coin_value_data)
    max_value = max(coin_value_data)
    avg_value = round(sum(coin_value_data) / len(coin_value_data), 2)

    x = PrettyTable()
    x.field_names = [" ", "AVG", "MIN", "MAX"]
    # "SD", "Q1", "Q2", "Q3", "RNG", "IQR", "UPS", "DOWNS", "LUP", "LDWN"
    x.add_row([api_response_data['symbol'], avg_value, min_value, max_value])

    print(x)


crypto_list = []
data_list = []
statistics_list = []


def show_data_all_coins(key):
    end_point_url = f"https://api.basecampcrypto.nl/v1/coin?key={key}"

    api_get_request = requests.get(url=end_point_url)

    api_response_data = eval(api_get_request.text)

    for item in api_response_data:
        crypto_list.append(item)

    for item in crypto_list:
        end_point_url = f"https://api.basecampcrypto.nl/v1/coin/{item['symbol']}/history?key={key}"

        api_get_request = requests.get(url=end_point_url)

        api_response_data = eval(api_get_request.text)
        data_list.append(api_response_data)

    for crypto_name in crypto_list:
        for crypto in data_list:
            value_list = []
            for day in crypto['history']:
                value_list.append(day['value'])
            total_average = 0
            for value in value_list:
                total_average += value

            coin_stats = {}
            coin_stats['name'] = crypto['symbol']
            coin_stats['average'] = round(total_average / 365, 2)
            coin_stats['min'] = min(value_list)
            coin_stats['max'] = max(value_list)
            coin_stats['stand_dev'] = round(statistics.stdev(value_list), 2)

            quartile_list = numpy.percentile(value_list, [25, 50, 75])
            coin_stats['quart_1'] = round(quartile_list[0], 2)
            coin_stats['median'] = round(quartile_list[1], 2)
            coin_stats['quart_3'] = round(quartile_list[2], 2)
            coin_stats['inter_q_range'] = round(quartile_list[2] - quartile_list[0], 2)

            coin_stats['range'] = round(max(value_list) - min(value_list), 2)

            total_up_counter = 1
            total_down_counter = 0
            long_up_counter = 0
            long_down_counter = 0
            longest_up = 0
            longest_down = 0
            for x in range(len(value_list) - 1):
                if value_list[x + 1] > value_list[x]:
                    if long_down_counter > longest_down:
                        longest_down = long_down_counter
                    long_down_counter = 0
                    long_up_counter += 1
                    total_up_counter += 1
                else:
                    if long_up_counter > longest_up:
                        longest_up = long_up_counter
                    long_up_counter = 0
                    long_down_counter += 1
                    total_down_counter += 1

            coin_stats['ups'] = total_up_counter
            coin_stats['downs'] = total_down_counter
            coin_stats['lup'] = longest_up
            coin_stats['ldown'] = longest_down

            statistics_list.append(coin_stats)
        return statistics_list


def statisctics_table_create(key):
    statistics_list = show_data_all_coins(key)
    statistics_table = PrettyTable(
        [" ", "AVG", "MIN", "MAX", "SD", "Q1", "Q2", "Q3", "RNG", "IQR", "UPS", "DOWNS", "LUP", "LDWN"])
    for coin_stat in statistics_list:
        statistics_table.add_row(
            [coin_stat['name'], coin_stat['average'], coin_stat['min'], coin_stat['max'], coin_stat['stand_dev'],
             coin_stat['quart_1'], coin_stat['median'], coin_stat['quart_3'], coin_stat['range'],
             coin_stat['inter_q_range'], coin_stat['ups'], coin_stat['downs'], coin_stat['lup'], coin_stat['ldown']])
    print(statistics_table)


def alice_stocks():
    money = 1000000
    stocks = 0
    alb_data = data_list[0]
    value_list = []
    for day in alb_data['history']:
        value_list.append(day['value'])
    for value in value_list:
        if value < 1500 and stocks == 0:
            stocks = money / value
            money = 0
        elif value > 1600 and money == 0:
            money = stocks * value
            stocks = 0
    if money == 0:
        money = value_list[364] * stocks
        stocks = 0
    return round(money, 2)


def bob_stocks():
    money = 1000000
    stocks = 0
    bha_data = data_list[1]
    value_list = []
    for day in bha_data['history']:
        value_list.append(day['value'])
    for value in value_list:
        if value < 1000 and stocks == 0:
            stocks = money / value
            money = 0
        elif value > 1100 and money == 0:
            money = stocks * value
            stocks = 0
    if money == 0:
        money = value_list[364] * stocks
        stocks = 0
    return round(money, 2)


def carol_stocks():
    money = 1000000
    stocks = 0
    cas_data = data_list[2]
    value_list = []
    for day in cas_data['history']:
        value_list.append(day['value'])

    for x in range(len(value_list) - 1):
        if value_list[x + 1] < value_list[x]:
            going_up = False
        elif value_list[x + 1] > value_list[x]:
            going_up = True
        if going_up and stocks == 0:
            stocks = money / value_list[x]
            money = 0
        if not going_up and money == 0:
            money = stocks * value_list[x]
            stocks = 0
    if money == 0:
        money = value_list[364] * stocks

    return round(money, 2)


def dave_stocks():
    money = 1000000
    stocks = 0
    cas_data = data_list[3]
    value_list = []
    for day in cas_data['history']:
        value_list.append(day['value'])
    for x in range(len(value_list) - 3):
        if value_list[x + 1] < value_list[x] and value_list[x + 2] < value_list[x + 1] and value_list[x + 3] \
                < value_list[x + 2] and stocks == 0:
            stocks = money / value_list[x + 3]
            money = 0
        if value_list[x + 1] > value_list[x] and value_list[x + 2] > value_list[x + 1] and value_list[x + 3] \
                > value_list[x + 2] and money == 0:
            money = stocks * value_list[x + 3]
            stocks = 0
    if money == 0:
        money = value_list[364] * stocks
        stocks = 0
    return round(money, 2)


def eve_stocks():
    money = 1000000
    stocks = 0
    cas_data = data_list[4]
    value_list = []
    for day in cas_data['history']:
        value_list.append(day['value'])

    counter = 0
    for x in range(len(value_list)):
        if x + 1 == counter + 1 and stocks == 0:
            stocks = money / value_list[x]
            money = 0
        if x + 1 == counter + 5 and money == 0:
            money = value_list[x] * stocks
            stocks = 0
            counter += 10
    if money == 0:
        money = value_list[364] * stocks
    return round(money, 2)


def frank_stocks():
    money = 1000000
    stocks = 0
    cas_data = data_list[5]
    value_list = []
    for day in cas_data['history']:
        value_list.append(day['value'])

    stocks = money / value_list[0]
    money = 0
    sell_value = value_list[0]

    for value in value_list:
        if value >= sell_value * 1.20 and stocks == 0:
            stocks = money / value
            money = 0
            sell_value = value
        if value <= sell_value * 0.8 and money == 0:
            money = stocks * value
            stocks = 0
            sell_value == value
    if money == 0:
        money = value_list[364] * stocks
    return round(money, 2)


def create_csv():
    list = []
    counterlist = []
    for x in range(1, 366):
        counterlist.append(x)
    list.append(counterlist)
    for crypto in data_list:
        cryptolist = []
        for day in crypto['history']:
            cryptolist.append(day['value'])
        list.append(cryptolist)
    data = PrettyTable(["Day", "ALB", "BHA", "CAS", "DUB", "ELG", "FAW", "XUA", "YIL", "ZOS"])
    for x in range(365):
        data.add_row(
            [list[0][x], list[1][x], list[2][x], list[3][x], list[4][x], list[5][x], list[6][x], list[7][x],
             list[8][x], list[9][x]])
    with open('test.csv', 'w', newline='') as file:
        file.write(data.get_csv_string())


#qx95gdbja26sZa5P

if __name__ == '__main__':
    request = requests.get('https://api.basecampcrypto.nl/')
    node_key = "qx95gdbja26sZa5P"
    statisctics_table_create(node_key)
    while True:
        print("[1] Get Team Data")
        print("[2] Get Coins data")
        print("[3] Get Single Coin Value")
        print("[4] Get Single Coin Value History")
        print("[5] Table")
        print("[6] Investors")

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
            get_single_coin_value(node_key, node_symbol)
        elif user_input == "4":
            node_key = input('Team key: ')
            node_symbol = input('Coin Symbol: ')
            get_single_coin_value_history(node_key, node_symbol)
        elif user_input == "5":

            node_key = "qx95gdbja26sZa5P"
            statisctics_table_create(node_key)
        elif user_input == "6":
            print(f"Alice Money: {alice_stocks()} Euro")
            print(f"Bob Money: {bob_stocks()} Euro")
            print(f"Carol Money: {carol_stocks()} Euro")
            print(f"Dave Money: {dave_stocks()} Euro")
            print(f"Eve Money: {eve_stocks()} Euro")
            print(f"Frank Money: {frank_stocks()} Euro")
        elif user_input == "7":
            create_csv()
        elif user_input == "8":
            create_csv()
        elif user_input == "10":
            quit()
