"""
    AppleGame
    In deze game kan je random apples verdienen maar ook verliezen
    Dit doe je door random te gebruiken.

    random.randint(0,10) //Dit geeft een getal tussen  0, en 11
    time.sleep(5) // gebruik dit om het lees baar te houden

    - (optioneel) Zorg dat de spelers upgrades kunnen kopen.
    - (Verplicht) Bij een aantal appels heeft de speler gewonnen.
    - (optioneel) Zorg er voor dat de speler kan verliezen als hij geen appels meer heeft.
    - (optioneel) Zet er moeilijkheids niveaus er in.



"""


import random
import time
totaal_aantal_appels = random.randint(1,3)



while True:
    time.sleep(2)

    totaal_aantal_appels = totaal_aantal_appels + random.randint(1, 3)
    totaal_aantal_appels = totaal_aantal_appels - random.randint(1, 3)

    if(totaal_aantal_appels <= 0):
        print('game over')
        exit()

    if(totaal_aantal_appels == 10):
        print('je hebt gewonnen kut hoer')
        exit()

    print(f'{totaal_aantal_appels}')
