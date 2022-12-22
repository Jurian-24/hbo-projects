import os
import json

cwd = os.getcwd()

fileData = open(cwd + '/movies.json')
fileData = json.load(fileData)


def main() -> None:
    print("[I] Movie information overview")
    print("[M] Make modification based on assignment")
    print("[S] Search a movie title ")
    print("[C] Change title and/or release year by search on title")
    print("[Q] Quit program")

    userChoice = input('Enter your choice: ').upper()

    if userChoice == 'I':
        moviesIn2004 = len([movie for movie in fileData if movie['year'] == 2004])

        numberOfScienceFictionMovies = len([
            movie for movie in fileData if 'Science Fiction' in movie['genres']
        ])

        keanuReevesMovies = [movie for movie in fileData if 'Keanu Reeves' in movie['cast']]

        sylvesterStalloneMovies = [movie['title'] for movie in fileData
            if 'Sylvester Stallone' in movie['cast'] and 1995 <= movie['year'] <= 2005]

        print(f'Movies in 2004: {moviesIn2004}')
        print(f'Science fiction movies: {numberOfScienceFictionMovies}')
        print(f'Keanu Reeve movies: {keanuReevesMovies}')
        print(f'Sylvester Stallone movies between 1995 and 2005: {sylvesterStalloneMovies}')

        main()
    elif userChoice == 'M':

        main()
    elif userChoice == 'S':
        movieName = input('Enter the movie you want to search').title()
        movies = movie_info_overview(movieName)
        if len(movies) > 1:
            for index, movie in enumerate(movies):
                print(f"[{index}] {movie['title']} {movie['year']}")

            selectMovie = int(input('Enter the number of the movie you want to see: '))

            print(movies[selectMovie])

        print(movies[0])
        main()
    # Implement rest of functionality


def movie_info_overview(movieTitle):
    return [movie for movie in fileData if movie['title'] == movieTitle]


if __name__ == "__main__":
    main()
