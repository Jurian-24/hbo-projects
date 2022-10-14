'''
The following data reprsents average tempratures of the third month for 1995, 2010, and 2020 recorded in Amsterdam.
Implement a program that given this data prints the answers for the following questions (each seperate line):
	- How many days have equal average tempratues in March 1995 and March 2010.
	- How many days have equal average tempratues in March 1995 and March 2020.
	- Which year has a day with highest temprature in March?
	- Which year had the warmest March?
'''

temperatures = (
    ('1995', '3', ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4', '40.5',
     '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0']),
    ('2010', '3', ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9', '42.7',
     '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6']),
    ('2020', '3', ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0', '48.9',
     '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'])
)


def compareSets(list1, list2):
    set_difference = set(list1) - set(list2)
    list_difference = list(set_difference)

    for difference in list_difference:
        list1 = list(list1)
        list1.remove(difference)

    return len(list1)


def getHighestTemp(returnYear):
    highestTemp = 0
    highestTempYear = 0

    for year in temperatures:
        sortedTempratures = sorted(year[2], reverse=True)

        if float(sortedTempratures[0]) > highestTemp:
            highestTemp = float(sortedTempratures[0])
            highestTempYear = int(year[0])

    if returnYear:
        return highestTempYear

    return highestTemp


def warmestMonth(setOfTempratures):
    averageTemp = 0
    highestAverageYear = 0

    for year in setOfTempratures:

        for i in range(len(year[2])):
            year[2][i] = float(year[2][i])

        yearAverage = sum(year[2]) / len(year[2])

        if yearAverage > averageTemp:
            averageTemp = yearAverage
            highestAverageYear = year[0]

    return highestAverageYear


temprature1995 = set(temperatures[0][2])
temprature2010 = set(temperatures[1][2])
temprature2020 = set(temperatures[2][2])

if __name__ == '__main__':
    print(compareSets(temprature1995, temprature2010))
    print(compareSets(temprature1995, temprature2020))
    print(getHighestTemp(True))
    print(warmestMonth(temperatures))
