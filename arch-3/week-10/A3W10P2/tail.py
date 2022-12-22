import os

if __name__ == '__main__':
    cwd = os.getcwd()
    for textFileNumber in range(1, 4):
        fileFound = False

        try:
            fhand = open(cwd + f'/random0{textFileNumber}.txt')
            fileFound = True
        except not fhand:
            print('No such file')

        if fileFound:
            if textFileNumber == 1:
                fileLines = []

                for line in fhand:
                    fileLines.append(next(fhand).strip('\n'))

                for line in range(10):
                    print(fileLines[len(fileLines)-line])

            elif textFileNumber == 2:
                lengthFile = sum(1 for line in fhand)

                for line in range(lengthFile - 10, lengthFile):
                    print(fhand.readline(line))
            elif textFileNumber == 3:
                print()

