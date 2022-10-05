"""
A string is a palindrome if it is identical forward and backward.
For example “anna”, “civic”, “level” and “hannah” are all examples of palindromic words.
Write a program that reads a string from the user and uses a loop to determines whether or not it is a palindrome.
Display the result, including a meaningful output message.
"""

palindrome = input('Enter a palindrome: ')

if(palindrome == palindrome[::-1]):
    print('It is a palindrome.')
else:
    print('It`s not a palindrome')
