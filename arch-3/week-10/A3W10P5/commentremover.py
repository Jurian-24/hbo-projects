import os

if __name__ == '__main__':
    cwd = os.getcwd()

    fileInput = input('Enter the file: ')

    try:
        fhand = open(cwd + f'/{fileInput}')
    except Exception:
        print(f'No such file as: {fileInput}')
        exit()

    newFileContent = []

    for line in fhand:
        commentFound = False
        newLine = ''

        for char in line:
            if char == '#':
                commentFound = True
                break

            newLine += char

        newFileContent.append(newLine)

    newFileInput = input('Enter the file you want to store it to (incl extension): ')

    newFile = open(newFileInput, 'x+')
    newFile = open(newFileInput, 'w')

    for line in newFileContent:
        newFile.write(line)
    newFile.close()
