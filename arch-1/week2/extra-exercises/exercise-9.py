# Problem 4-9*: evaluating teacher
# The students are evaluating their teacher with the grade [1 - 10].
# If the teacher scores 10, then (s)he is EXCEPTIONAL.
# If the teacher scores [7-9], then (s)he is GOOD.
# For grades in interval [4-6], the teacher is AVERAGE.
# If the teacher scores 3 or less, then (s)he is bad.
# Make an algorithm that will input the score and the salary for the teacher.
# Then, check if the score is valid (in range [1-10]) and if not, print that the input is wrong.
# Otherwise, print what kind of a teacher (s)he is, update and print the salary according to the following formula:
# Exceptional teacher gets 15% raise.
# Bad teachers have his / her salary reduced to 85%.
# Every other type of teacher gets the raise in percentage equivalent to his / her score (e.g. grade 8 means 8% increase, grade 4 means 4% increase, …)

teachersGrade = int(input('Enter the grade you want the give to your teacher: '))
teacherTitle = ''

if(0 < teachersGrade < 10):
    # Give the teacher a title based off the grade (s)he receives
    if(teachersGrade < 3):
        teacherTitle = 'bad'
    elif(4 <= teachersGrade <= 6):
        teacherTitle = 'average'
    elif(7 <= teachersGrade <= 9):
        teacherTitle = 'good'
    elif(teachersGrade == 10):
        teacherTitle = 'exceptional'

    # Increase or reduce salary based of the title
    if(teacherTitle == 'exceptional'):
        salaryRaise = '15% more'
    elif(teacherTitle == 'bad'):
        salaryRaise = '85%'
    else:
        salaryRaise = str(teachersGrade) + '% more'

    print(f'You are a {teacherTitle} teacher and your salary will be {salaryRaise} in comparison of your last salary')
else:
    print('You can only enter a number between 1-10')


