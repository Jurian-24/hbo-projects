"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
All 3 sides of an equilateral triangle have the same length.
An isosceles triangle has two sides that are the same length, and a third side that is a different length.
If all of the sides have different lengths then the triangle is scalene.

Write a program that reads the lengths of 3 sides of a triangle from the user. Display a message indicating the type of the triangle.
"""
import re

sides = input('')

sides = sides.split(",")

side1 = int(re.search(r'\d+', sides[0]).group())
side2 = int(re.search(r'\d+', sides[1]).group())
side3 = int(re.search(r'\d+', sides[2]).group())


if(side1 == side2 == side3):
    print('equilateral')
elif(side1 == side2 or side2 == side3 or side3 == side1):
    print('isosceles')
else:
    print('scalene')

