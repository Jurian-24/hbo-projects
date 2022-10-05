"""
Write a program that draws “modular rectangles” like the ones below.
The user specifies the width and height of the rectangle, and the entries start at 0 and increase typewriter fashion from left to right and top to bottom,
but are all done mod 10. Example: Below are examples of a 3 x 5 rectangular:

0 1 2 3 4
5 6 7 8 9
0 1 2 3 4
"""

height = int(input('Enter the height: '))
width = int(input('Enter the width: '))

counter = 0

heightCounter = 0

while heightCounter < height:
    widthCounter = 0

    while widthCounter < width:
        if widthCounter == width:
            widthCounter = 0
        elif counter == 10:
            counter = 0
        print(f'{counter}', end=" ")

        counter += 1
        widthCounter += 1

    print()
    heightCounter += 1

# rows = int(input("Please Enter the Total Number of Rows  : "))
# columns = int(input("Please Enter the Total Number of Columns  : "))

# print("Hollow Rectangle Star Pattern")
# i = 0
# while(i < rows):
#     j = 0
#     while(j < columns):
#         if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
#             print('*', end = '  ')
#         else:
#             print(' ', end = '  ')
#         j = j + 1
#     i = i + 1
#     print()
