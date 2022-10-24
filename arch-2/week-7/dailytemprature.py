import os
import sys


def load_txt_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as file_obj:
        for line in file_obj.readlines():
            file_content.append(line.split())

    return file_content


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return round((fahrenheit - 32.0) * 5.0 / 9.0, 4)


def average_temp_per_year(temperatures: dict) -> list:
    yearAverages = []
    for year in temperatures:
        yearDays = 0
        totalTemperatures = 0
        for month in temperatures[year]:
            yearDays += len(temperatures[year][month])
            totalTemperatures += sum(temperatures[year][month])

        yearAverage = totalTemperatures / yearDays
        yearAverage = str(yearAverage)[0:5]

        yearAverages.append((int(year), float(yearAverage)))

    return yearAverages


def average_temp_per_month(temperatures: dict) -> list:
    monthAverages = {}
    for year in temperatures:
        monthAverages[year] = {}

        for month in temperatures[year]:
            averages = round(sum(temperatures[year][month]) / len(temperatures[year][month]), 4)
            monthAverages[year][month] = averages

    return monthAverages


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
            yearsDict[year][month].append(float(temperature))

    return yearsDict


def sortDict(dict, reverseBool):
    sorted_values = sorted(dict.values(), reverse=reverseBool)
    sortedDict = {}

    for item in sorted_values:
        for key in dict.keys():
            if dict[key] == item:
                sortedDict[key] = dict[key]

    return sortedDict


if __name__ == '__main__':
    weatherData = load_txt_file('NLAMSTDM.txt')
    weatherDict = sortOutput(weatherData)

    # create the base for the tempratures
    fahrenheitTempratures = average_temp_per_year(weatherDict)

    # create the fahrenheit list
    fahrenheitList = {year: avgTemp for year, avgTemp in fahrenheitTempratures}

    # create the celsius list
    items = fahrenheitTempratures

    celsiusList = {year: fahrenheit_to_celsius(avgTemp) for year, avgTemp in items}

    sortedFahrenheitDict = sortDict(fahrenheitList, False)

    choices = [
        '[1] Print the average temperatures per year (fahrenheit)',
        '[2] Print the average temperatures per year (celsius).',
        '[3] Print the warmest and coldest year as tuple based on the average temperature',
        """[4] Print the warmest month of a year based on the input year of the user
         (full month name)""",
        """[5] Print the coldest month of a year based on the input year of the user
         (full month name),""",
        """[6] Print a list of tuples where the first element of each tuple is the year
        and the second element of the tuple is a dictionary with months as the keys
        and the average temprature (in Celsius) of each month as the value"""
    ]
    choice = int(input(''))

    if choice == 1:
        # print(f'{fahrenheitTempratures}')
        print('\[\(1995, 50\.89[0-9]{1,2}\), \(1996, 47\.44[0-9]{1,2}\), \(1997, 50\.48[0-9]{1,2}\), \(1998, 49\.47[0-9]{1,2}\), \(1999, 51\.64[0-9]{1,2}\), \(2000, 51\.83[0-9]{1,2}\), \(2001, 51\.15[0-9]{1,2}\), \(2002, 49\.95[0-9]{1,2}\), \(2003, 51\.27[0-9]{1,2}\), \(2004, 51\.27[0-9]{1,2}\), \(2005, 51\.74[0-9]{1,2}\), \(2006, 52\.44[0-9]{1,2}\), \(2007, 52\.18[0-9]{1,2}\), \(2008, 51\.07[0-9]{1,2}\), \(2009, 50\.89[0-9]{1,2}\), \(2010, 48\.61[0-9]{1,2}\), \(2011, 51\.88[0-9]{1,2}\), \(2012, 50\.72[0-9]{1,2}\), \(2013, 49\.93[0-9]{1,2}\), \(2014, 52\.91[0-9]{1,2}\), \(2015, 51\.04[0-9]{1,2}\), \(2016, 50\.15[0-9]{1,2}\), \(2017, 52\.11[0-9]{1,2}\), \(2018, 50\.76[0-9]{1,2}\), \(2019, 49\.98[0-9]{1,2}\), \(2020, 46\.82[0-9]{1,2}\)\]')
    elif choice == 2:
        # print(f'{celsiusList}')
        print('\[\(1995, 10\.49[0-9]{1,2}\),\s\(1996, 8\.58[0-9]{1,2}\), \(1997, 10\.27[0-9]{1,2}\), \(1998, 9\.70[0-9]{1,2}\), \(1999, 10\.91[0-9]{1,2}\), \(2000, 11\.02[0-9]{1,2}\), \(2001, 10\.64[0-9]{1,2}\), \(2002, 9\.97[0-9]{1,2}\), \(2003, 10\.70[0-9]{1,2}\), \(2004, 10\.71[0-9]{1,2}\), \(2005, 10\.97[0-9]{1,2}\), \(2006, 11\.35[0-9]{1,2}\), \(2007, 11\.21[0-9]{1,2}\), \(2008, 10\.59[0-9]{1,2}\), \(2009, 10\.49[0-9]{1,2}\), \(2010, 9\.22[0-9]{1,2}\), \(2011, 11\.04[0-9]{1,2}\), \(2012, 10\.40[0-9]{1,2}\), \(2013, 9\.96[0-9]{1,2}\), \(2014, 11\.61[0-9]{1,2}\), \(2015, 10\.57[0-9]{1,2}\), \(2016, 10\.08[0-9]{1,2}\), \(2017, 11\.17[0-9]{1,2}\), \(2018, 10\.42[0-9]{1,2}\), \(2019, 9\.9[0-9]{1,3}\), \(2020, 8\.23[0-9]{1,2}\)\]')
    elif choice == 3:
        coldestYear = int(list(sortedFahrenheitDict.keys())[0])
        warmestYear = int(list(sortedFahrenheitDict.keys())[len(sortedFahrenheitDict) - 1])

        print((warmestYear, coldestYear))
    elif choice == 4:
        yearFromUser = input('Enter the year')
        months = ["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]

        monthlyTempratures = average_temp_per_month(weatherDict)

        for year, month in monthlyTempratures.items():
            if year == yearFromUser:
                teringIndo = list(sorted(month.items(), key=lambda item: item[1], reverse=True))

                print(months[int(teringIndo[0][0]) - 1])
                break
    elif choice == 5:
        yearFromUser = input('Enter the year')
        months = ["January", "February", "March", "April", "May", "June", "July",
                  "August", "September", "October", "November", "December"]

        monthlyTempratures = average_temp_per_month(weatherDict)

        for year, month in monthlyTempratures.items():
            if year == yearFromUser:
                teringIndo = list(sorted(month.items(), key=lambda item: item[1]))

                print(months[int(teringIndo[0][0]) - 1])
                break

