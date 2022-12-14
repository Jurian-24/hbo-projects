from carparking import *
from datetime import datetime, timedelta

# Test for a normal check-in with correct result (True)
def test_check_in_capacity_normal():
    return
# Test for a check-in with maximum capacity reached (False)
def test_check_in_capacity_reached():
    return
# Test for checking the correct parking fees
def test_parking_fee():
    # Assert that parking time 2h10m, gives correct parking fee
    # Assert that parking time 24h, gives correct parking fee
    # Assert that parking time 30h == 24h max, gives correct parking fee
    return
# Test for validating check-out behaviour
def test_check_out():
    # Assert that {license_plate} is in parked_cars
    # Assert that correct parking fee is provided when checking-out {license_plate}
    # Aseert that {license_plate} is no longer in parked_cars
    cpm_mid = CarParkingMachine(hourly_rate=6)
    cpm_mid.check_in(license_plate='DDD')

    assert True == ('DDD' in cpm_mid.parked_cars)
    assert 6.0 == cpm_mid.check_out(license_plate='DDD')

    return

test_check_out
