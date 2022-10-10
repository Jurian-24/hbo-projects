'''
Implement a Python program that collects book information. The program starts with three options:
entering new book, searching a book, exit.

* Entering new book: The program will ask to enter: book title, book author, publisher, publication date.
  Input will be (comma seperated, single line). A book title can only be added to the list once (no duplication)
* Searching a book: The user enters a term and the program must search the term within titles, authors
  and publishers and report the existence of such a book with the requested term.
  - Create a function called: `search_book(books, term)` which will True or False on a match or not
* use a list of dictionaries for datastorage with the following attribute fields: [title, author, publisher, pub_date]
* create a menu structure that asks for the option to perform (A = add book, S = Search book, E = Exit (and print))
'''
