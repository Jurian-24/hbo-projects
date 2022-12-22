import os
import sys
import csv

def load_csv_data(fileName):
    file_content = []

    with open(os.path.join(sys.path[0], fileName), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))

    return file_content


def sortData(data):
    sortedData = []
    data.remove(data[0])

    for item in data:
        newShow = {}
        newShow = {
            'Id': item[0],
            'Game': item[1],
            'Series': item[2],
            'Country': item[3],
            'Details': item[4],
            'Ban Category': item[5],
            'Ban Status': item[6],
            'Wikipedia Profile': item[7],
            'Image': item[8],
            'Summary': item[9],
            'Developer': item[10],
            'Publisher': item[11],
            'Genre': item[12],
            'Homepage': item[13]
        }

        sortedData.append(newShow)

    return sortedData

# We created the menu layout for you
# Only given imports are allowed
def main(filename: str) -> None:
    data = load_csv_data(filename)
    sortedData = sortData(data)

    print("[I] Print request info from assignment")
    print("[M] Make modification based on assignment")
    print("[A] Add new game to list")
    print("[O] Overview of banned games per country")
    print("[S] Search the dataset by country")
    print("[Q] Quit program")

    userChoice = input('What do you want to do? ').upper()

    if userChoice == 'I':
        bannedInIsrael = len([ban for ban in sortedData if ban['Country'] == 'Israel'])

        countries = [ban['Country'] for ban in sortedData]
        countriesDict = {country: countries.count(country) for country in countries}
        countriesDict = dict(sorted(countriesDict.items(), key=lambda item: item[1], reverse=True))

        acBans = len([ban for ban in sortedData if ban['Series'] == "Assassin's Creed"])

        bansInGermany = [ban for ban in sortedData if ban['Country'] == 'Germany']

        redDeadBans = [ban['Country'] for ban in sortedData if ban['Game'] == 'Red Dead Redemption']

        print(f'How many games got banned in Israel? {bannedInIsrael}')
        print(f'Which country got the most games banned? {[countriesDict.keys()][0]}')
        print(f'AC bans: {acBans}')
        print(f'Bans in Germany: {bansInGermany}')
        print(f'Red dead bans: {redDeadBans}')

        main(filename)

    elif userChoice == 'M':
        pass
    elif userChoice == 'A':
        pass
    elif userChoice == 'O':
        # countrySearch = input('Enter the name of the country: ')

        bansOfCountry = [ban for ban in sortedData if ban['Country'] == 'Brazil']

        print(f'Brazil - {len(bansOfCountry)}')
        print(bansOfCountry)

        main(filename)
    elif userChoice == 'S':
        countrySearch = input('Enter the name of the country: ').capitalize()

        bansOfCountry = [ban for ban in sortedData if ban['Country'] == countrySearch]

        for game in bansOfCountry:
            print(f"{game['Game']} - {game['Details']}")

        main(filename)
    elif userChoice == 'Q':
        exit()

    # Implement rest of functionality

if __name__ == "__main__":
    main("bannedvideogames.csv")
