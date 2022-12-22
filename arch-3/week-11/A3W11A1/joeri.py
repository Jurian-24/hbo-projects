from datetime import datetime, timedelta
import json

parked_cars = {}


class ParkedCar:
    def __init__(self, license_plate, check_in):
        self.license_plate = license_plate
        self.check_in = check_in.replace(microsecond=0)


class CarParkingMachine:
    def __init__(self, id=None, capacity=10, hourly_rate=2.5):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.logger = CarParkingLogger()

    def check_in(self, license_plate, check_in=datetime.now()):
        if len(self.parked_cars) != self.capacity:
            if license_plate not in self.parked_cars:
                park_car = ParkedCar(license_plate, check_in)
                self.parked_cars[park_car.license_plate] = park_car
                self.logger = CarParkingLogger(self.id, check_in, license_plate)
                self.logger.car_check_in_log()
                return True
            else:
                print("Car already registered")
                return False
        else:
            return False

    def check_out(self, license_plate, check_out_fee=False):
        parked_car = self.parked_cars.get(license_plate, False)

        file_name = f"{self.id}_state.json"
        file = open(file_name, encoding="utf8")
        check_in_dict = json.load(file)
        file.close()

        with open(file_name, 'w') as json_log:
            for check_in in check_in_dict:
                if check_in["license_plate"] == license_plate:
                    check_in_dict.remove(check_in)
            check_in_dict = []
            json.dump(check_in_dict, json_log)
        json_log.close()

        if not parked_car:
            return False
        now = datetime.now()
        difference_in_seconds = (now - parked_car.check_in).total_seconds()
        hours = int(difference_in_seconds) / 3600
        if hours >= 24:
            hours = 24
            parking_fee = self.hourly_rate * hours
        else:
            hours = round(int(difference_in_seconds) / 3600)
            parking_fee = round(self.hourly_rate + self.hourly_rate * hours, 2)
        self.parked_cars.pop(license_plate)
        self.logger.car_check_out_log(license_plate, parking_fee)
        return parking_fee

    def get_parking_fee(self, license_plate):
        return self.check_out(license_plate, True)


class CarParkingLogger:
    def __init__(self, id=None, date=datetime.now(), license_plate=None):
        self.id = id
        self.date = date
        self.license_plate = license_plate
        self.log_check_in = ''

    def car_check_in_log(self):
        with open('carparklog.txt', "w") as log_file:
            log_text = f"{self.date.strftime('%Y-%m-%d %H:%M:%S')};cpm_name={self.id};" \
                       f"license_plate={self.license_plate};action=check-in"
            log_file.write(log_text + '\n')
            self.log_check_in = log_text
        log_file.close()

        check_in_dict = [{"license_plate": self.license_plate, "check_in": self.date.strftime('%Y-%m-%d %H:%M:%S')}]
        new_file_name = f"{self.id}_state.json"
        print(new_file_name)
        with open(new_file_name, 'w') as json_log:
            json.dump(check_in_dict, json_log)
        json_log.close()

    def car_check_out_log(self, license_plate, parking_fee):
        self.license_plate = license_plate
        with open('carparklog.txt', "w") as log_file:
            log_text = f"{self.date.strftime('%Y-%m-%d %H:%M:%S')};cpm_name={self.id};" \
                       f"license_plate={self.license_plate};action=check-out;" \
                       f"parking_fee={parking_fee}"
            log_file.write(self.log_check_in + '\n')
            log_file.write(log_text + '\n')
        log_file.close()
... (40 regels over)
