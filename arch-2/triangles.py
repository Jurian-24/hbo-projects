"""
If you have 3 straws, possibly of differing lengths, it may or may not be possible to lay them down so that they form a triangle when their ends are touching.
For example, if all of the straws have a length of 6 inches. then one can easily construct an equilateral triangle using them. However,
if one straw is 6 inches. long, while the other two are each only 2 inches. long, then a triangle cannot be formed.
In general, if any one length is greater than or equal to the sum of the other two then the lengths cannot be used to form a triangle.
Otherwise they can form a triangle. Write a function called "check_triangle" that determines whether or not three lengths can form a triangle.
The function will take 3 parameters and return a Boolean result.
In addition, write a program that reads 3 lengths from the user and demonstrates the behaviour of this function, on a correct triangle print possible otherwise impossible.
"""

def check_triangle(sideA, sideB, sideC):
    sides = [sideA, sideB, sideC]
    sides = sorted(sides, reverse=True)

    if(sides[1] + sides[2] <= sides[0]):
        print('impossible')
        return False
    else:
        print('possible')
        return True


if __name__ == '__main__':
    sideA = int(input('Enter side A'))
    sideB = int(input('Enter side B'))
    sideC = int(input('Enter side C'))

    check_triangle(sideA, sideB, sideC)
