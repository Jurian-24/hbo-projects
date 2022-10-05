# Problem 4-7*: prize money
# Three Informatica students are representing Hogeschool Rotterdam on an international programming competition.
# Each of the three students is getting a score that can be any whole number in the interval [0 - 5], and the total points the team gets is the sum of all three scores.
# The prize is directly dependant on the total score.
# If the team gets more than 10 points, then the prize is two times the product of their scores.
# If not, then the prize is just the product of their scores.
# The students have decided to split the prize money in the following way: if the prize is divisible by 3, they all get the same share.
# Otherwise, they get the proportion equal to their contribution in the sum of all scores (e.g. 2 + 3 + 8 = 13; 13 is not divisible by 3; the first gets 2/13 of the prize, the second 3/13 of the prize, the third 8/13 of the prize).
# Design an algorithm that will ask the user to input three scores of the students, then print out the total prize money, and how much money should each student get.

studentPoints = []

for i in range(3):
    pointsStudent = int(input(f'Enter your points student {i + 1}: '))

    if(0 > pointsStudent > 5):
        print('You can`t enter a number lower than 0 or above 5')
        exit()

    studentPoints.append(pointsStudent)

totalScore = sum(studentPoints)
if(totalScore > 10):
    priceMoney = totalScore * 2
else:
    priceMoney = totalScore

if(priceMoney % 3 != 0):
    for i in range(3):
        priceMoneyPerStudent = priceMoney * (studentPoints[i] / 13)
        print(f'The total price of your team is: {priceMoney}. Your share is {priceMoneyPerStudent:.2f}, student {i + 1}')

else:
    print(f'The teams total price is: {priceMoney}. Each of the students get {priceMoney / 3 :.2f}')
