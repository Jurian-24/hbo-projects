import os
if __name__ == '__main__':
    cwd = os.getcwd()
    text_name = input('Enter the file name: ')

    for fileNumber in range(1, 4):
        with open(cwd + f'/{text_name}', 'r') as fileData:
            wordsList = fileData.read().split()
            longestWordLength = len(max(wordsList, key=len))

        result = [textWord for textWord in wordsList if len(textWord) == longestWordLength]
        print(result)
