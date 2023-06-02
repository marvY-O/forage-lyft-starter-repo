class CarriganTires():
    def __init__(self):
        pass

    def needs_service(self, tires_wear):
        for tire in tires_wear:
            if (tire >= 0.9):
                return True  
        return False