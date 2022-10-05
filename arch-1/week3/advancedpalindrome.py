"""
There are numerous phrases that are palindromes when spacing is ignored.
Examples include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others.
Write a program that it ignores spacing while determining whether or not a string is a palindrome.
"""

palindrome = input()

palindromeWithoutSpaces = palindrome.replace(' ', '')

if(palindromeWithoutSpaces == palindromeWithoutSpaces[::-1]):
    print('It is a palindrome.')
else:
    print('is not a palindrome')
