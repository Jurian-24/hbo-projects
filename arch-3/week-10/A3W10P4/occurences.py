import os
if __name__ == '__main__':
    textFileInput = input('Enter the file: ')

    cwd = os.getcwd()
    filefound = False

    try:
        fileData = open(cwd + f'/{textFileInput}')
    except Exception:
        print(f'No such file as {textFileInput}')
        exit()

    wordsList = fileData.read().split()
    wordsDict = {}

    for word in wordsList:
        word = word.lower()

        if word not in wordsDict:
            wordsDict[word] = 1
        else:
            wordsDict[word] += 1

    print(wordsDict)
