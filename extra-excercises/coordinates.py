xCoord = float(input('Enter your X coordinate: '))
yCoord = float(input('Enter your Y coordinate: '))

if xCoord < 0 and yCoord < 0:
    print('linksonder')
elif xCoord > 0 and yCoord > 0:
    print('rechtsboven')
elif xCoord > 0 and yCoord < 0:
    print('rechtsonder')
elif xCoord < 0 and yCoord > 0:
    print('rechtsboven')
else:
    print('Wrong input')

print(f"{'rechts' if xCoord > 0 else 'links'}{'boven' if yCoord > 0 else 'onder'}")
