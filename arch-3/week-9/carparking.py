from datetime import datetime

# ParkedCar class to store information of parked cars.


class ParkedCar:
    def __init__(self, license_plate: str, time: datetime):
        self.license_plate = license_plate
        self.time = time

class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def check_in(self, license_plate: str, time=datetime.now()):
        if len(self.parked_cars) >= self.capacity:
            return False

        parked_car = ParkedCar(license_plate, time)
        self.parked_cars[parked_car.license_plate] = parked_car

        return True

    def check_out(self, license_plate: str, check_fee=False):

        parked_car = self.parked_cars.get(license_plate, False)

        if not parked_car:
            return False

        now = datetime.now()
        differenceInSeconds = (now - parked_car.time).total_seconds()
        hours = int(differenceInSeconds) / 3600

        rate = f'{(self.hourly_rate + (self.hourly_rate * hours)):.2f}'

        if not check_fee:
            self.parked_cars.pop(license_plate)

        return rate

    def get_parking_fee(self, license_plate):
        return self.check_out(license_plate, True)


def main(CarParkingMachine):
    choices = [
        '[I] Check-in car by license plate',
        '[O] Check-out car by license plate',
        '[Q] Quit program'
    ]

    for choice in choices:
        print(choice)

    userChoice = input('Enter your choice: ').upper()

    if userChoice == 'I':
        license_plate = input('Enter the license_plate: ')

        check_in = CarParkingMachine.check_in(license_plate)

        if check_in:
            print('License registered')
            main(CarParkingMachine)
            return

        print('Capacity reached!')
    elif userChoice == 'O':
        license_plate = input('Enter the license_plate: ')

        check_out = CarParkingMachine.check_out(license_plate)

        if check_out:
            print(f'Parking fee: {check_out} EUR')
            main(CarParkingMachine)
            return

        print(f'License plate {license_plate} not found')
        main(CarParkingMachine)
        return



    elif userChoice == 'Q':
        return
    else:
        return 'Please enter a valid choice'

if __name__ == "__main__":
    main(CarParkingMachine())
