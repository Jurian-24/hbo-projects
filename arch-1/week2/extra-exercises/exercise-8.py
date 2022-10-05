# Problem 4-8: green lantern

# The Green Lantern's ring is searching the Earth for a new candidate to recruit into the Corps.
# When it finds a new candidate, it will check the gender (use standard input: ‘m’ for male and ‘f’ for female).
# If the candidate is a male, the ring will look for age and weight. If it is a female, the ring will look for age and height.
# To recruit the candidate into the Corps, a male must be younger than 40, and his weight must not be over 80.
# For female candidates, she must be over 20 years of age and taller than 160.
# Design an algorithm that will check the gender of the candidate.
# Then, depending on the outcome, input the needed values and make the decision whether to recruit or not.

gender = input('Put your gender in m/f: ')

if(len(gender) == 1):
    if(gender == 'm'):
        age = int(input('Enter your age: '))
        weight = int(input('Enter your weight in kg: '))
        if(age >= 40 and weight >= 80):
            print('You can be recruited')
        else:
            print('You cant be recruited')
    elif(gender == 'f'):
        age = int(input('Enter your age: '))
        height = int(input('Enter your height in cm: '))
        if(age >= 20 and height >= 160):
            print('You can be recruited')
        else:
            print('You cant be recruited')
    else:
        print('Your gender doesn`t exist')
