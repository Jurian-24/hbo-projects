"""
A data file containing Netflix title is provided.
Implement your solution in a program that meets the following requirements:

- The program gets the file name as a program argument.
- Use the function `load_csv_file` to load the content of the file in a list.
- The first line of the file specifies the name of each column.
  For example, the first column is show_id, the second is the type of the show, etc...
  Create a function called `get_headers(file_content)` that returns a list
  of all the columns from the first row (explore the kind of information you can extract)
- Make a function `search_by_type(file_content, show_type)`
  that returns a list of all TV Shows or Movies based on the requested type
  * Make use of `lambda` for the solution
- Make a function `search_by_director(file_content, director)`
  that returns a list of all TV Shows and Movies that have that director
  * Make use of `lambda` for the solution
- Make a function `get_directors(file_content)`
  that returns a set of directors in the list (use set for single directors only)
- Within the main function ask the user for an input, use the following options:
  [1] Print the amount of TV Shows
  [2] Print the amount of Movies
  [3] Print the (full) names of directors in alphabetical order who lead both tv shows and movies.
      (for example, search the name David Ayer. He is the director of three movies and one tv show)
  [4] Print the name of each director in alphabetical order,
      the number of movies and the number of tv shows (s)he was the director of.
      Use a tuple with format: (director name, number of movies, number of tv shows) to print.
"""

import os
import sys
import csv

def removeArrayBrackets(string):
    string = str(string).replace("[", '')
    string = str(string).replace("]", '')
    string = str(string).replace("'", '')

    return string

def load_csv_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))

    return file_content


def sortData(data):
    sortedData = []
    data.remove(data[0])

    for item in data:
        newShow = {}
        newShow = {
            'show_id': item[0],
            'type': item[1],
            'title': item[2],
            'director': item[3],
            'cast': item[4],
            'country': item[5],
            'date_added': item[6],
            'release_year': item[7],
            'rating': item[8],
            'duration': item[9],
            'listed_in': item[10],
            'description': item[11],
        }

        sortedData.append(newShow)

    return sortedData


def get_directors(file_content) -> set:
    # if not isinstance(file_content, dict):
    #     file_content = sortData(file_content)

    shows = file_content
    directors = {'director'}

    for show in shows:
        directors.add(show['director'])

    directors.discard('director')

    return directors


def get_headers(file_content) -> list:
    # if not isinstance(file_content, dict):
    #     file_content = sortData(file_content)

    return file_content[0]

def search_by_type(file_content, show_type):

    # if not isinstance(file_content, dict):
    #     file_content = sortData(file_content)

    shows = []
    list(filter(lambda x: shows.append(x['title']) if x['type'] == show_type else '', file_content))

    return shows

def search_by_director(file_content, director):
    # if not isinstance(file_content, dict):
    #     file_content = sortData(file_content)

    moviesOfDirector = []
    list(
        filter(
            lambda x: moviesOfDirector.append(x['title'])
            if x['director'] == director else '',
            file_content
        )
    )

    return moviesOfDirector

def get_movieType(file_content, movie):
    # if not isinstance(file_content, dict):
    #     file_content = sortData(file_content)

    movieType = []

    list(
        filter(
            lambda x: movieType.append(x['type'])
            if x['title'] == movie else '',
            file_content
        )
    )

    return removeArrayBrackets(movieType)


def main(netflixData):
    # Sort the data into a dictonary
    netflixData = sortData(netflixData)
    choices = [
        '[1] Print the amount of TV Shows',
        '[2] Print the amount of Movies',
        '[3] Print the (full) names of directors with a movie and show',
        '[4] Print the director with the movies and shows'
    ]

    for choice in choices:
        print(choice)

    choiceUser = int(input(''))

    if choiceUser == 1:
        print(len(search_by_type(netflixData, 'TV Show')))
    elif choiceUser == 2:
        print(len(search_by_type(netflixData, 'Movie')))
    elif choiceUser == 3:
        directors = get_directors(netflixData)

        movieDirectorWithBothTypes = []

        for director in directors:
            moviesOfDirector = search_by_director(netflixData, director)

            if director != '':
                directorMovieTypes = {director}

                for movie in moviesOfDirector:

                    movieType = get_movieType(netflixData, movie)

                    directorMovieTypes.add(movieType)

                    if 'TV Show' in directorMovieTypes and 'Movie' in directorMovieTypes:
                        movieDirectorWithBothTypes.append(director)

        print(sorted(set(movieDirectorWithBothTypes)))
    elif choiceUser == 4:
        directors = get_directors(netflixData)

        movieDirectorWithBothTypes = []

        for director in directors:
            moviesOfDirector = search_by_director(netflixData, director)

            if director != '':
                directorMovieTypes = {director}
                showCount = 0
                movieCount = 0

                for movie in moviesOfDirector:

                    movieType = get_movieType(netflixData, movie)

                    directorMovieTypes.add(movieType)

                    if movieType == 'TV Show':
                        showCount += 1
                    elif movieType == 'Movie':
                        movieCount += 1

                movieDirectorWithBothTypes.append((director, movieCount, showCount))

        print(sorted(set(movieDirectorWithBothTypes)))

    else:
        print('Error: You didnt enter a right value')


if __name__ == '__main__':
    netflixData = load_csv_file('netflix_titles.csv')
    main(netflixData)
