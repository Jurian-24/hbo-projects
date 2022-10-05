# Problem 4-5: analysis lessons

# The course of Analysis 1 consists of 12 lessons, 6 theoretical and 6 practical.
# During 6 teaching weeks, two lessons per week are given, always starting with the theoretical and then followed by the practical lesson.
# Therefore, in week 1, lessons 1 and 2 are given; in week 2, lessons 3 and 4 are given; in week 3, lessons 5 and 6 are given; and so on … where lessons 1, 3, 5, … are theoretical and lessons 2, 4, 6, … are practical.
# You task it to design an algorithm that will input the lesson number (integer 1-12).
# If the number is not valid, you should output the appropriate message (e.g. “invalid input”).
# For valid lesson number, print in which week the lesson is given and is it a theoretical or a practical one.

numberOfLessons = int(input('Number of lessons: '))
counter = 0
weekNumber = 1

if(1 > numberOfLessons > 12):
    print('Error: You have to put in a minimum of 1 lesson and a maximum of 12 lessons')

for i in range(numberOfLessons):
    i = i + 1

    if(counter == 2):
        counter = 0
        weekNumber = weekNumber + 1

    if(i % 2 == 1):
        lessonType = 'Theoretical'
    else:
        lessonType = 'Practical'

    counter = counter + 1

    print(f'Week: {weekNumber} \nLesson number: {i} \nLesson type: {lessonType} \n')
