from mine.Car import Car
from Engines.WilloughbyEngine import WilloughbyEngine
from Engines.CapuletEngine import CapuletEngine
from Engines.SternmanEngine import SternmanEngine

from Batteries.SpindlerBattery import SpindlerBattery
from Batteries.NubbinBattery import NubbinBattery

class CarFactory():
    def __init__(self):
        pass

    def create_calliope(current_date, last_service_date, current_milage, last_service_milage):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_glissdale(current_date, last_service_date, current_milage, last_service_milage):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_rorschach(current_date, last_service_date, current_milage, last_service_milage):
        engine = WilloughbyEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def create_thovex(current_date, last_service_date, current_milage, last_service_milage):
        engine = CapuletEngine(last_service_milage, current_milage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car