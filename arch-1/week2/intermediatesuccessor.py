""""
Write a program that reads a date from the user and computes its immediate successor.
For example, if the user enters values that represent 2013-11-18 then your program should display a message indicating that the day immediately after 2013-11-18 is 2013-11-19.
If the user enters values that represent 2013-11-30 then the program should indicate that the next day is 2013-12-01.
If the user enters values that represent 2013-12-31 then the program should indicate that the next day is 2014-01-01.

- The date will be entered in YYYY-MM-DD format.
- Assume there is no leap year and February is always 28 days.
- The program must print Input format ERROR. Correct Format: YYYY-MM-DD in case the user enters an incorrect input. Some examples of incorrect input: 2013/12/30,2013_12_30, 0213/12/30, 30-12-2013.
- Input example: Input Date: 2013-12-31 , Output example: Next Date: 2014-01-01
"""

date = input('Enter a date: ')

day = date[8:10]
month = date[5:7]
year = date[0:4]
fullMonths = [1, 3, 5, 7, 8, 10, 12]
maxDays = 31

if month == '02':
    maxDays = 28
elif int(month) not in fullMonths:
    maxDays = 30

if int(day) > maxDays:
    print('ERROR: the max days in the chosen month are: ' + str(maxDays) + '. Try again.')
else:
    if '-' not in year:
        if day == '31' and month == '12':
            date = f'{int(year) + 1}-01-01'
            print('Next date:' + date)
            exit()
        if int(month) >= 9:
            if int(day) < maxDays:
                if(int(day) <= 9):
                    date = f'{year}-{month}-0{int(day) + 1}'
                else:
                    date = f'{year}-{month}-{int(day) + 1}'
                print('Next Date: ' + date)
            elif int(month) == 9:
                date = f'{year}-{int(month) + 1}-01'
                print('Next Date: ' + date)
            elif int(month) >= 10:
                date = f'{year}-{int(month) + 1}-01'
                print('Next Date: ' + date)

        elif int(day) == maxDays:
            date = f'{year}-{int(month) + 1}-01'
            print('Next Date: ' + date)
        else:
            date = date.replace(day, str(int(day) + 1))
            date = f'{year}-{month}-{int(day) + 1}'

            print('Next Date: ' + date)
    else:
        print('Input format ERROR. Correct Format: YYYY-MM-DD')
