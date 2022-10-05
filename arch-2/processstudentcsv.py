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
import datetime

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
    user = line.split(',')

    user = [{
        'number': user[0],
        'first_name': user[1],
        'last_name': user[2],
        'date': user[3],
        'program': user[4]
    }]

    if studentNumberCheck(user['number']) and studentNumberCheck(user['first_name']) and studentNumberCheck(user['last_name']) and studentNumberCheck(user['date']) and dateChecker(user['number']):
        print('goede user a mattie')
    else:
        print('verkeerde user a mattie')

def studentNumberCheck(number):
    print(number)

def studentNameCheck(name):
    print(name)

def studentProgramCheck(program):
    print(program)

def dateChecker(date):
    print(date)

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
