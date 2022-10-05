import random

"""
A primary school teacher needs to automate basic arithmetic (summation, multiplication table, subtraction) exercises for her students.
You are asked to implement a program that asks what type of the arithmetic the user needs to practice.
Then, the program will generate exercises and the user should give the result. Consider the following features for the program:

For each arithmetic operation keep the total number of the exercises 10.

The program must be interactive: for example, if the chosen exercise is multiplication table,
then the program generates two random numbers (check how python can generate random integers: Week 01: Step 01, Exercise 2, Code 4),
like 3 and 5; the program prints 3 * 5 = and the user must give the result; the program will print if the answer was correct
or wrong and then the program will generate next question.

Your program must be implemented with a function `arithmetic_operation(type)`,
which can create a sum for each arithmetic operation based on the input given by a user (summation, multiplication, subtraction).

Numbers for summation and subtractions will be between 1 and 100.

For other aspects of the program feel free to decide your choice.
- Extented version: Extend your program such that it collects all the mistakes from the user and prints them at the end.
- Extented version: The teacher would like to know which questions are difficult for her students. Extend your program such that it measures the time that the students takes to answer each question. For each question collect the information in a tuple like (question, correct or wrong,time). The program collects all the results in a list and prints them at the end.
- Extented version: Sort the list of the results based on their time before printing it.
"""

def arithmetic_operation(arithmeticType):

    wrongAnswers = []

    for question in range(1, 11):

        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)

        if arithmeticType == 'summation':
            answer = int(input(f'{number1} + {number2} = '))
            if answer == number1 + number2:
                print('Right answer')
            else:
                print('Wrong answer')
                wrongAnswers.append(question)
        elif arithmeticType == 'multiplication':
            answer = int(input(f'{number1} * {number2} = '))
            if answer == number1 * number2:
                print('Right answer')
            else:
                print('Wrong answer')
                wrongAnswers.append(question)
                print(wrongAnswers)
        elif arithmeticType == 'substraction':
            answer = int(input(f'{number1} - {number2} = '))
            if answer == number1 - number2:
                print('Right answer')
            else:
                print('Wrong answer')
                wrongAnswers.append(question)
        else:
            print('Error: you can only choose between: substraction, multiplication, summation')
            break

    print('You got the following questions wrong:')
    for wrongAnswer in wrongAnswers:
        print(wrongAnswer)

arithmeticType = input('Enter the type of arithmetic table you want: ')

if __name__ == '__main__':
    arithmetic_operation(arithmeticType)
