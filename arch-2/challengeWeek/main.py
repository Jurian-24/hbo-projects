import json
import time
import requests
from tkinter import *
# from sense_hat import SenseHat


def responseCheck(response):
    try:
        assert response.status_code == 200
    except:
        print('Cant load the data at this moment.')
        return False

def getAllWeatherData():
    response = requests.get("https://api.basecampserver.tech/sensors")

    responseCheck(response)

    data = json.loads(response.text)

    return data

def getDataById(node_id):
    response = requests.get(f'https://api.basecampserver.tech/sensors?node_id={node_id}')

    responseCheck(response)

    data = json.loads(response.text)

    return data


def createNode(title, description):
    endPoint = 'https://api.basecampserver.tech/nodes'

    node = {
        "name": title,
        "description": description
    }

    r = requests.post(url = endPoint, json = node)

    # Response is a string, transform it into a dict
    responseData = json.loads(r.text)

    nodeId = responseData['id']
    nodeKey = responseData['key']

    return startApp(nodeId, nodeKey)

def postWeatherData(node_id, node_key):
    # sense = SenseHat()
    endPoint = f'https://api.basecampserver.tech/sensors?key={node_key}'
    # get the weather data from the sense hat

    # temp = sense.temp
    temp_value = 16

    # pressure = sense.pressure
    pressure_value = 20

    # humidity = sense.humidity
    humidity_value = 64

    weatherData = {
        "timestamp": time.time(),
        "temperature": temp_value,
        "humidity": humidity_value,
        "pressure": pressure_value,
        "node_id": node_id
    }

    r = requests.post(url = endPoint, json = weatherData)

    return startApp(node_id, node_key)

def startApp(nodeId='', nodeKey=''):
    choices = [
        '[1] Get all the data from the archive',
        '[2] Get specific data from the archive by id',
        '[3] Create new node',
        '[4] Create new weather data with the last created node',
        '[5] Exit'
    ]

    for choice in choices:
        print(choice)

    userChoice = input('Enter the thing you want to do: ')

    if userChoice == '1':
        data = getAllWeatherData(nodeId, nodeKey)
        print(data)
        startApp(nodeId, nodeKey)
    elif userChoice == '2':
        nodeId = input('Enter the id of which data set you want to find: ')

        print(getDataById(nodeId, nodeKey))
        startApp(nodeId, nodeKey)
    elif userChoice == '3':
        nodeTitle = input('Enter the title of the node: ')
        nodeDescription = input('Enter the description of the node: ')

        createNode(nodeTitle, nodeDescription)
    elif userChoice == '4':
        postWeatherData(nodeId, nodeKey)
    elif userChoice == '5':
        return

if __name__ == '__main__':
    startApp()
