"""
Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns.
The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the internet .
"""

celsius = 10

print('C | F')
while celsius < 100:
    fahrenheit = (celsius * 9.0/5.0) + 32.0
    print(f'{celsius} {fahrenheit:.0f}')
    celsius += 10
