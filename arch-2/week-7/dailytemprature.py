"""
A data file containing average daily tempreture of Amsterdam is used.
The first column is the month number, the second is the day number,
the third is the year and fourth column is the weather tempretaure in Farenheit.
Implement your solution to meet the following requirements:

- The program gets the file name as a program argument.
- Use the function `load_txt_file` to load the content of the file in a list.
  Adjust this function or add a new one to clean the content of the loaded list.
  Like: remove new line character, split each line.
  Use the following format for the storage: `{year: {month: [temp, temp, temp]}, ...}`
- Create a function `fahrenheit_to_celsius(fahrenheit: float) -> float` that given the value in
  fahrenheit returns the celsius representitive (rounding is not needed)
- Create a function `average_temp_per_year(temperatures: dict) -> list` that
  processes the data and calculates the average temprature per year.
  Return a list of tuples (year, average temprature).
- Create a function `average_temp_per_month(temperatures: dict) -> list`
  this function should return the average temperature per month based on the provided list
  Tip: provide a `temperatures` per year to have the averages per month per year
- Within the main function ask the user for an input, use the following options:
  [1] Print the average temperatures per year (fahrenheit)
  [2] Print the average temperatures per year (celsius) Hint: Use built-in map() function.
  [3] Print the warmest and coldest year as tuple based on the average temperature
  [4] Print the warmest month of a year based on the input year of the user (full month name)
  [5] Print the coldest month of a year based on the input year of the user (full month name)
  [6] Print a list of tuples where the first element of each tuple is the year and
      the second element of the tuple is a dictionary with months as the keys and
      the average temprature (in Celsius) of each month as the value
"""
import os
import sys


def load_txt_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())

    return file_content


def sortOutput(weatherData):
    yearsDict = {}

    for data in weatherData:
        year = data[2]
        month = data[0]
        temperature = data[3]

        if year not in yearsDict:
            yearsDict[year] = {}

        if month not in yearsDict[year]:
            yearsDict[year][month] = []

        if temperature not in yearsDict[year][month]:
            yearsDict[year][month].append(temperature)

    return yearsDict


if __name__ == '__main__':
    weatherData = load_txt_file('NLAMSTDM.txt')
    print(sortOutput(weatherData))
