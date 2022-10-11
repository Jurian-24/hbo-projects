bookList = {}


def addBook(bookList):
    # bookData = input('Enter the name, author, publisher and the publication date of the book: ')
    bookData = input('')

    if bookData.count(',') == 3:
        bookData = bookData.split(',')
        if bookData[0] in bookList:
            print('Error: Book already in the library')
            startApp(bookList)

        if '' in bookData:
            print('error: Try again')
            startApp(bookList)
        else:
            bookList = {
                'title': bookData[0],
                'author': bookData[1],
                'publisher': bookData[2],
                'pub_date': bookData[3]
            }
            print(bookList)

            startApp(bookList)
    else:
        print('error: Try again')
        startApp(bookList)


def search_book(books, term):
    bookFound = False
    if term == '':
        term = input('Enter the name of the book you want to find')

    for bookInfo in books:
        if term in bookInfo.values():
            bookFound = True
            print('found')

    return bookFound


def exitProgram(bookList):
    print(bookList)
    exit()


def startApp(bookList):
    if __name__ == '__main__':
        # choice = input('Press A: to add a book, S: to save a book or E: to exit the program ').lower()
        choice = input('').lower()

        if choice == 'a':
            addBook(bookList)
        elif (choice == 's'):
            search_book(bookList, '')
        elif (choice == 'e'):
            exitProgram(bookList)
        else:
            print('Not an option. Try again')


startApp(bookList)
