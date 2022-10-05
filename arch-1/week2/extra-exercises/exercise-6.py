# Problem 4-6: year end bonus

# Your company wants to calculate the bonuses of employees.
# Bonus is related to gross annual salary of each employee.
# For those employees who earn below 30.000 per year bonus will be 10%, for those between 30.000 and less than 40.000 will be 12%, between 40.000 and less than 55.000 will be 14% and for all others will be 15%.
# For any given employee’s salary, the program should calculate the exact amount of end-year bonus.
# Design the algorithm, create the flowchart, test all conditions and implement it in Python.

salary = int(input('Enter your salary: '))
bonus = 0

if(salary < 30000):
    bonus = salary * 0.10
elif(30000 < salary < 40000):
    bonus = salary * 0.12
elif(40000 < salary < 55000):
    bonus = salary * 0.14
elif(salary > 55000):
    bonus = salary * 0.15

print(f'Your bonus will be {bonus:.0f} this year')
