"""
A dataset is given with information of students: student number, first name, last name, date of birth, study program.
You are asked to implement a program that given this dataset (as a csv file), the program processes the information. The requested criteria are:
Sometimes data values are corrupted. The program must report corupted values. Any invalid or empty value is defined as corrupted.

- Student number has this format: 7 digits, starting with 0 and second digit (from left) can be either 9 or 8. Example: 0212345 is not valid
- First name and last names, contains only alphabet.
- Date of birth has this format: YYYY-MM-DD. Days between 1 and 31, months between 1 and 12 and Years between 1960 and 2004.
- Study program can have one of these values: INF, TINF, CMD, AI.

A template Python file is provided with a function that loads the data set.

The program should make two separate lists: list of rows with correct values and a list of rows with corrupted values.
These two lists will be printed with this format:
"""
import os
import sys

valid_lines = []
corrupt_lines = []

'''
The validate_data function will check the students.csv line by line for corrupt data.

- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.

Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.

Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:

0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']

In the above example the studentnumber does not start with '08' or '09',
the last name contains a special character and the student program is empty.

Don't forget to put the students.csv file in the same location as this file!
'''

def validate_data(line):
    invalidUserData = []

    userData = line.split(',')

    user = {
        'number': userData[0],
        'first_name': userData[1],
        'last_name': userData[2],
        'date': userData[3],
        'program': userData[4]
    }

    if studentNumberCheck(user['number']) and studentNameCheck(user['first_name']) and studentNameCheck(user['last_name']) and dateChecker(user['date']) and studentProgramCheck(user['program']):
        valid_lines.append(line)
        wrongData = False

    if studentNumberCheck(user['number']) == False:
        invalidUserData.append(user['number'])
        wrongData = True

    if studentNameCheck(user['first_name']) == False:
        invalidUserData.append(user['first_name'])
        wrongData = True

    if studentNameCheck(user['last_name']) == False:
        invalidUserData.append(user['last_name'])
        wrongData = True

    if studentProgramCheck(user['program']) == False:
        invalidUserData.append(user['program'])
        wrongData = True

    if dateChecker(user['date']) == False:
        invalidUserData.append(user['date'])
        wrongData = True

    if wrongData == True:
        invalidDataString = f'{user["number"]},{user["first_name"]},{user["last_name"]},{user["date"]},{user["program"]} => INVALID DATA: {invalidUserData}'
        corrupt_lines.append(invalidDataString)

def studentNumberCheck(number):
    if len(number) == 7:
        if(number[0] == '0'):
            if(number[1] == '9' or number[1] == '8'):
                if number.isnumeric():
                    return True
    return False

# - First name and last names, contains only alphabet.
def studentNameCheck(name):
    return name.isalpha()


# - Study program can have one of these values: INF, TINF, CMD, AI.
def studentProgramCheck(program):
    availablePrograms = ['INF', 'TINF', 'CMD', 'AI']

    return program in availablePrograms


# - Date of birth has this format: YYYY-MM-DD. Days between 1 and 31, months between 1 and 12 and Years between 1960 and 2004.
def dateChecker(date):

    if len(date) != 10:
        return False

    year, month, day = date.split('-')

    if 1960 <= int(year) <= 2004:
        if 1 <= int(day.lstrip('0')) <= 31:
            if 1 <= int(month.lstrip('0')) <= 12:
                return True

    return False

def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')
