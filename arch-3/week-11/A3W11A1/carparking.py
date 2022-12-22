import os
import json
from datetime import datetime
# ParkedCar class to store information of parked cars.
cwd = os.getcwd()
carParkingMachines = []

class ParkedCar:
    def __init__(self, license_plate: str, time: datetime):
        self.license_plate = license_plate
        self.time = time

class CarParkingMachine:
    def __init__(self, id, capacity=10, hourly_rate=2.50):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = CarParkingLogger(self).get_cars()

    def check_in(self, license_plate: str, time=datetime.now()):
        if len(self.parked_cars) >= self.capacity:
            return False

        for cpm in carParkingMachines:
            data = json.load(open(f'parking-machine-{cpm}-001.json'))

            for item in data:
                if item.keys() == license_plate:
                    print(f'This car is already registered at machine: {cpm}')
                    return
                else:
                    print(item.keys() == license_plate)

        cpl = CarParkingLogger(self, ParkedCar(license_plate, time))
        cpl.check_in()

        self.parked_cars = cpl.get_cars()

        return True

    def check_out(self, license_plate: str, check_fee=False):
        parked_car = ''
        # parked_car = self.parked_cars.get(license_plate, False)

        for item in range(len(self.parked_cars)):
            if self.parked_cars[item] == license_plate:
                parked_car = self.parked_cars[item]
                break
        if not parked_car:
            return False

        now = datetime.now()
        differenceInSeconds = (now - datetime.strptime(parked_car['check_in'], "%Y-%m-%d %H:%M:%S.%f")).total_seconds()
        hours = int(differenceInSeconds) / 3600

        rate = f'{(self.hourly_rate + (self.hourly_rate * hours)):.2f}'

        if not check_fee:
            # remove car from log
            # self.parked_cars.pop(license_plate)
            cpl = CarParkingLogger(self, parked_car)
            cpl.check_out()

        self.parked_cars = cpl.get_cars()

        return rate

    def get_parking_fee(self, license_plate):
        return self.check_out(license_plate, True)


class CarParkingLogger:
    def __init__(self, CarParkingMachine, ParkedCar=None):
        self.cpm = CarParkingMachine
        self.car = ParkedCar

    def check_in(self):
        # cars = [
        #     {
        #         "license_plate": "",
        #         "check_in": "",
        #     }
        # ]

        cars = [
            {
                f"{self.car.license_plate}": f"{self.car}",
            }
        ]

        cpmPath = f'parking-machine-{self.cpm.id}-001.json'

        if os.path.exists(cpmPath):
            with open(cpmPath, 'r') as file:
                prevJson = json.load(file)
                cars = prevJson + cars

        open(cpmPath, 'w').write(
            json.dumps(cars, sort_keys=True, indent=4, separators=(',', ': '))
        )
        # with open(cpmPath, "w") as file:
        #     json.dumps(cars, file, indent=4)


    def check_out(self):
        path = f'parking-machine-{self.cpm.id}-001.json'
        jsonObj = json.load(open(path))

        for item in range(len(jsonObj)):
            searchedPlate = jsonObj[item].get('license_plate')

            if searchedPlate == self.car['license_plate']:
                jsonObj.pop(item)
                break

        # update json file
        open(path, "w").write(
            json.dumps(jsonObj, sort_keys=True, indent=4, separators=(',', ': '))
        )


    def get_cars(self):
        path = f'parking-machine-{self.cpm.id}-001.json'

        if os.path.exists(path):
            data = json.load(open(path))
            return data

        return {}

def main(CarParkingMachine):
    carParkingMachines.append(CarParkingMachine.id)

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
    main(CarParkingMachine(id='North'))
