import os

def getFileName(fileName):
    fileName = os.path.splitext(fileName)[0]

    return fileName

"""
   mySum(a, b) Calculates the sum of two numbers
   example: mySum(1.0, 2.0) -> 3.0
   example: getFileName(main.py) -> main
   :param: a: First number
   :returns: the file name without the file extension
"""