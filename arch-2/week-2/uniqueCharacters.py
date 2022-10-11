'''
Implement a program that determines and displays the number of unique characters in a string
entered by the user. For example, Hello, World! has 10 unique characters while zzz has only
one unique character.

* Use only dictionaries to solve this problem (create a function: unique_chars_dict).
* Use only sets to solve this problem (create a function: unique_chars_set).
* Which solution would you prefer?
'''

def unique_chars_dict(string):
    characters = {}

    for char in string:
        characters[char] = True

    print(f'dic: {len(characters)} unique character(s)')

def unique_chars_set(string):
    characters = set(tuple(char) for char in string)
    print(f'{len(characters)} unique character(s)')

if __name__ == '__main__':
    userInput = input('Enter a word: ')
    unique_chars_dict(userInput)
    unique_chars_set(userInput)
