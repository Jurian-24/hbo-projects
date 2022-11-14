import json
import os
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext

import requests
import time
from prettytable import PrettyTable

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

# from sense_hat import SenseHat

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class AllDataInDatabase(Page):
   def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # content pf the page below

        Scrolledtext = scrolledtext.ScrolledText(self, state="disable")
        Scrolledtext.pack()

        response = requests.get(f'https://api.basecampserver.tech/sensors')

        data = json.loads(response.text)
        tableHeaders = {}

        for i in range(len(data)):
            for item in data[i].keys():
                tableHeaders.update({item: []})

        weatherData = {}
        for header in tableHeaders:
            weatherData[header] = []

        table = PrettyTable()

        for i in range(len(data)):
            for key, value in data[i].items():
                weatherData[key].append(f'{value:.0f}')

        table.title = f'All the results in the database:'
        table.field_names = tableHeaders

        for i in range(len(data)):
            newRow = []
            for value in data[i].values():
                newRow.append(f'{value:.0f}')

            table.add_row(newRow)

        #create table
        Scrolledtext.config(state="normal")
        Scrolledtext.delete("1.0", "end")
        Scrolledtext.insert(1.0, table)
        Scrolledtext.config(state="disable")

class GetDataById(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # content
        nodeIdLabel = Label(self, text='Enter the node id:')
        nodeIdLabel.pack()

        self.nodeId = Entry(self)
        self.nodeId.pack(side="top")

        searchButton = Button(self, text="Get Weather", command=self.getWeatherById)
        searchButton.pack()

        # create the base for the table
        self.Scrolledtext = scrolledtext.ScrolledText(self, state="disable")
        self.Scrolledtext.pack()

        self.fig = Figure(figsize = (5, 5), dpi = 100)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack()


    def getWeatherById(self):
        nodeId = self.nodeId.get()

        response = requests.get(f'https://api.basecampserver.tech/sensors?node_id={nodeId}')

        data = json.loads(response.text)

        tableHeaders = {}

        for i in range(len(data)):
            for item in data[i].keys():
                tableHeaders.update({item: []})

        weatherData = {}
        for header in tableHeaders:
            weatherData[header] = []

        table = PrettyTable()

        for i in range(len(data)):
            for key, value in data[i].items():
                weatherData[key].append(f'{value:.0f}')

        table.title = f'Results for node id: {nodeId}'
        table.field_names = tableHeaders

        for i in range(len(data)):
            newRow = []
            for value in data[i].values():
                newRow.append(f'{value:.0f}')

            table.add_row(newRow)

        #create table
        self.Scrolledtext.config(state="normal")
        self.Scrolledtext.delete("1.0", "end")
        self.Scrolledtext.insert(1.0, table)
        self.Scrolledtext.config(state="disable")

        # create graph
        temperatures = weatherData.get('temperature', 0)
        humidity = weatherData.get('humidity', 0)
        pressure = weatherData.get('pressure', 0)

        plot = self.fig.add_subplot(111)

        plot.plot(temperatures, label='Temperatures')
        plot.plot(humidity, label='Humidity')
        plot.plot(pressure, label='Pressure')

        plot.legend(loc="upper left")

        # clear the chart
        for item in self.canvas.get_tk_widget().find_all():
            self.canvas.get_tk_widget().delete(item)

        self.canvas.draw()

class CreateNewNodePage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        # content
        self.message = StringVar()
        self.messageLabel = Label(self, textvariable=self.message)
        self.messageLabel.pack()

        nodeTitleLabel = Label(self, text='Enter the node title')
        nodeTitleLabel.pack()

        self.nodeTitle = Entry(self)
        self.nodeTitle.pack(side="top")

        nodeDescriptionLabel = Label(self, text='Enter the node description')
        nodeDescriptionLabel.pack()

        self.nodeDescription = Text(self)
        self.nodeDescription.pack(side="top")

        searchButton = Button(self, text="Add node", command=self.createNode)
        searchButton.pack()


    def createNode(self):
        self.message.set('')

        endPoint = 'https://api.basecampserver.tech/nodes'

        node = {
            "name": str(self.nodeTitle.get()),
            "description": str(self.nodeDescription.get("1.0",END))
        }

        r = requests.post(url = endPoint, json = node)

        # Response is a string, transform it into a dict
        responseData = json.loads(r.text)

        nodeId = responseData['id']
        nodeKey = responseData['key']

        # set the node id and nodekey to the create data page for authentication
        os.environ['nodeId'] = str(nodeId)
        os.environ['nodeKey'] = str(nodeKey)

        self.message.set('You created a node. Head over to the add weather data tab to add new sensor data.')

        self.nodeTitle.delete(0, END)
        self.nodeDescription.delete('1.0', END)

        return

class CreateNewWeatherDataPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.temprature = 32
        self.pressure = 1009
        self.humidity = 48

        self.message = StringVar()
        self.messageLabel = Label(self, textvariable=self.message)
        self.messageLabel.pack()

        tempratureLabel = Label(self, text=f'Current temperature: {self.temprature}')
        tempratureLabel.pack()

        pressureLabel = Label(self, text=f'Current pressure: {self.pressure}')
        pressureLabel.pack()

        humidityLabel = Label(self, text=f'Current humidity: {self.humidity}')
        humidityLabel.pack()

        searchButton = Button(self, text="Add sensor data", command=self.addSensorData)
        searchButton.pack()

    def addSensorData(self):
        # sense = SenseHat()
        endPoint = f'https://api.basecampserver.tech/sensors?key={os.environ["nodeKey"]}'
        # get the weather data from the sense hat

        weatherData = {
            "timestamp": time.time(),
            "temperature": 80,
            "humidity": 90,
            "pressure": 100,
            "node_id": os.environ['nodeId']
        }

        r = requests.post(url = endPoint, json = weatherData)

        if r.status_code != 201:
            self.message.set('Something went wrong, try again later')
            return

        self.message.set(f'You uploaded new sensor data the to node with id: {os.environ["nodeId"]}')

        return


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        overviewPage = AllDataInDatabase(self)
        overviewPageById = GetDataById(self)
        createNodePage = CreateNewNodePage(self)
        addNewDataPage = CreateNewWeatherDataPage(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        # create navbar
        overviewPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        buttonToOverviewPage = tk.Button(buttonframe, text="Get all the temperatures", command=overviewPage.lift)
        buttonToOverviewPage.pack(side="left")

        overviewPageById.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        buttonToOverviewPageById = tk.Button(buttonframe, text="Get temperatures by node id", command=overviewPageById.lift)
        buttonToOverviewPageById.pack(side="left")

        createNodePage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        buttonToCreateNodePage = tk.Button(buttonframe, text="Create new node", command=createNodePage.lift)
        buttonToCreateNodePage.pack(side="left")

        addNewDataPage.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        buttonToAddNewDataPage = tk.Button(buttonframe, text="Create new node", command=addNewDataPage.lift)
        buttonToAddNewDataPage.pack(side="left")

        overviewPage.show()
        overviewPageById.show()
        addNewDataPage.show()
        createNodePage.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x600")
    root.mainloop()
