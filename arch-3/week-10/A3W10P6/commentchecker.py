import os

if __name__ == '__main__':
    cwd = os.getcwd()

    fileInput = input('Enter the file: ')
    fileInput = fileInput.split(',')

    for file in fileInput:
        fileNotFound = False
        try:
            fhand = open(cwd + f'/{file}')
        except Exception:
            print(f'No such file as: {file}')
            fileNotFound = True

        if not fileNotFound:
            for index, line in enumerate(fhand):
                if 'def' in line:
                    functionName = line.replace('def ', '')
                    functionName = functionName.replace(':', '')

                    if '#' not in fhand.readline():
                        print(f"""
                        File: {file} contains a function [{functionName}] on line [{index + 1}] without a preceding comment.
                        """)
