"""
Make a research about truth tables. Write down truth tables for "and" & "or".
Implement a program that prints these two truth tables.
"""

p = True
q = True

for i in range(2):
    q = bool(i)

    if(p == True and q == True):
        result = True
        print(f'{p} {q} {result}')
    else:
        result = False

    if(p == True or q == True):
        result = True
        print(f'{p} {q} {result}')
