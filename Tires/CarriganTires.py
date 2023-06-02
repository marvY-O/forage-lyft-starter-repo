from tire import Tire

class CarriganTires(Tire):
    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        for tire in self.tires_wear:
            if (tire >= 0.9):
                return True  
        return False