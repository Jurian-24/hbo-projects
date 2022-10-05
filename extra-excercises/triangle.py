height = int(input('Enter the height: '))
width = int(input('Enter the width: '))

i = 0

while(i < height):
    j = 0

    while(j < width):
        if(i == height):
            i = 0
            height += 1
            print('\n')
        print(i, end=" ")
        i += 1
        j += 1
