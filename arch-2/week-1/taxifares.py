"""
In a particular jurisdiction, taxi fares consist of a base fare of 4.00 eur, plus 0.25 eur for every 140 meters traveled.
Write a function called "calculate_fare"that takes the distance traveled (in kilometers) as its only parameter and returns the total fare as its only result.
Write a main program that interacts with the user and calls the function to produce and print the final result.
"""

def calculate_fare(distance):
    distance = round((distance * 1000) / 140, 0)
    totalAmount = 4.00 + (0.25 * (distance + 1))

    return totalAmount

if __name__ == '__main__':
    distance = float(input('Enter the distance of the trip: '))
    print(calculate_fare(distance))

