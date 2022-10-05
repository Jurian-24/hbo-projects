celsiusDegrees = float(input('How many degrees: '))

if(celsiusDegrees >= 20 and celsiusDegrees <= 29):
    print('Het is warm')
elif(celsiusDegrees <= 0):
    print('Het vriest')
elif(celsiusDegrees >= 1 and celsiusDegrees <= 10):
    print('het is koud')
elif(celsiusDegrees >= 11 and celsiusDegrees <= 19):
    print('het is lekker weer')
elif(celsiusDegrees >= 30 and celsiusDegrees <= 42):
    print('het is te heet')
elif(celsiusDegrees > 70.7):
    print('onmogelijk')
