"""
The Twelve Days of Christmas is a repetitive song that describes an increasingly long list of gifts sent to one’s true love on each of 12 days.
A single gift is sent on the first day. A new gift is added to the collection on each additional day, and then the complete collection is sent.
The first three verses of the song are shown below. The complete lyrics are available on the internet.

    On the first day of Christmas my true love sent to me: A partridge in a pear tree.

    On the second day of Christmas my true love sent to me: Two turtle doves, And a partridge in a pear tree.

    On the third day of Christmas my true love sent to me: Three French hens, Two turtle doves, And a partridge in a pear tree.


Your task is to write a program that displays the complete lyrics for The Twelve Days of Christmas.
Write a function named "next_verse" that takes the verse number as its only parameter and displays the specified verse of the song.
Then call that function 12 times with integers that increase from 1 to 12. Each item that is sent to the recipient in the song should only appear once in your program,
with the possible exception of the partridge. It may appear twice if that helps you handle the difference between “A partridge in a pear tree” in the first verse and
“And a partridge in a pear tree” in the subsequent verses.
"""

def next_verse(verseNumber):
    presents = [
        "A partridge in a pear tree",
        "Two turtledoves ",
        "Three french hens,",
        "Four calling Birds,",
        "Five gold rings (five golden rings),",
        "Six geese a-laying,",
        "Seven swans a-swimming,",
        "Eight maids a-milking,",
        "Nine ladies dancing,",
        "Ten lords a-leaping,",
        "Eleven pipers piping,",
        "Twelve drummers drumming,"
    ]

    newVerse = []
    startVerse = f'On the {verseNumber}st day of Christmas, my true love sent to me '
    if verseNumber > 1:
        startVerse = f'On the {verseNumber}nd day of Christmas, my true love sent to me '
        presents[0] = 'And a partridge in a pear tree'

    for i in range(verseNumber):
        newVerse.insert(0, presents[i])

    for i in newVerse:
        startVerse += i

    print(startVerse)


if __name__ == '__main__':
    for verse in range(1, 13):
        next_verse(verse)
