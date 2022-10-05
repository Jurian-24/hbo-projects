"""
In this exercise you will create a program that displays a multiplication table that shows the products
of all combinations of integers from 1 times 1 up to and including 10 times 10.
Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10.
It should also include labels down the left side consisting of the numbers 1 through 10.
"""

for i in range(1, 11):
    print(i, end=' ')
    for j in range(1, 11):
        print(f'{i * j}', end=' ')
    print('\n')

