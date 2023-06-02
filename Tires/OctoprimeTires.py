from tire import Tire

class OctoprimeTires(Tire):
    def __init__(self, tires_wear):
        self.tires_wear = tires_wear

    def needs_service(self):
        if (sum(self.tires_wear) >= 3):
            return True
        else:
            return False