from engine import Engine

class WilloughbyEngine(Engine):
    def __init__(self, last_service_milage, current_milage):
        self.last_service_milage = last_service_milage
        self.current_milage = current_milage    
    
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
    