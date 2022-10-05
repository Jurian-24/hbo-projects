"""
Make a list of national holidays in The Netherlands (assume current year).
Write a program that reads a month and day from the user.
If the month and day match one of the holidays in the list then your program should display the holiday's name.
Otherwise your program should indicate that the entered month and day do not correspond to a fixed-date holiday.
"""

month = input('Month: ')
day = input('Day: ')

if(month + '-' + day == '1-1'):
    print('Holiday: Nieuwjaarsdag')
elif(month + '-' + day == '4-15'):
    print('Holiday: Goede vrijdag')
elif(month + '-' + day == '4-17' or month + '-' + day == '4-18'):
    print('Holiday: Pasen')
elif(month + '-' + day == '4-27'):
    print('Holiday: Koningsdag')
elif(month + '-' + day == '5-5'):
    print('Holiday: Bevrijdingsdag')
elif(month + '-' + day == '5-26'):
    print('Holiday: Hemelvaartsdag')
elif(month + '-' + day == '6-5' or month + '-' + day == '6-6'):
    print('Holiday: Pinksteren')
elif(month + '-' + day == '12-25' or month + '-' + day == '12-26'):
    print('Holiday: Kerstmis')
