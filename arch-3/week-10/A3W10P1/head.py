import os

if __name__ == '__main__':
    cwd = os.getcwd()
    for textFileNumber in range(1, 4):

        try:
            fhand = open(cwd + f'/random0{textFileNumber}.txt')
            for i in range(10):
                print(next(fhand).strip('\n'))
        except not fhand:
            print('No such file')

