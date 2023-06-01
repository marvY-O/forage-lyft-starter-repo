from abc import ABC, abstractmethod

from mine.Servicable import Servicable
from mine.Engine import Engine
from mine.Battery import Battery

class Car(Servicable, ABC):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    @abstractmethod
    def needs_service(self):
        pass
