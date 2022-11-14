from datetime import datetime, timedelta


class CarParkingMachine:
    def __init__(self, capacity=10, hourly_rate=2.50):
        self.capicity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = dict()

    def check_in(self, license_plate, start_time):
        start_time = datetime.now()
        if len(self.parked_cars) < self.capicity:
            self.parked_cars[license_plate] = ParkedCar(license_plate, start_time)
            return True
        return False

    def check_out(self, license_plate):
        parked_car = self.parked_cars.get(license_plate, False)

        if not parked_car:
            return 'No car found with that license plate'

        end_time = datetime.now()

        timedelta = parked_car.check_in - end_time

        whole_parking_seconds = timedelta.seconds
        whole_parking_hours = 0

        if whole_parking_hours < 3600:
            whole_parking_hours = 1
        elif whole_parking_seconds > 86400:
            whole_parking_hours = 24
        else:
            whole_parking_hours = whole_parking_seconds // 3600

        del self.parked_cars[license_plate]

        return self.hourly_rate * whole_parking_hours


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in


def main():
    carparkingmachine_1 = CarParkingMachine()
    while True:
        menu_list = ["[I] Check-in car by license plate", "[O] Check-out car by license plate", "[Q] Quit program"]
        for choice in menu_list:
            print(choice)
        input_user = input("Please make a choice: ")
        if input_user == "I" or input_user == "i":
            license_plate = input("Please enter a license plate: ")
            if carparkingmachine_1.check_in(license_plate, datetime.now()):
                print("License registered")
            else:
                print("Capacity reached")
        elif input_user == "O" or input_user == "o":
            input_user = input("Please enter a license plate: ")
            parking_fee = carparkingmachine_1.check_out(input_user)
            print(f"Parking fee: {parking_fee:.2f} EUR")
        elif input_user == "Q" or input_user == "q":
            break
        elif input_user == "S" or input_user == "s":
            for x in carparkingmachine_1.parked_cars:
                print(carparkingmachine_1.parked_cars[x])


if __name__ == "__main__":
    main()
