import unittest

from Tires.CarriganTires import CarriganTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_tires = [0.1, 0.5, 1.0, 0.9]
        battery = CarriganTires()
        self.assertTrue(battery.needs_service(wear_tires))

    def test_needs_service_false(self):
        wear_tires = [0.8, 0.3, 0.4, 0.8]
        battery = CarriganTires()
        self.assertTrue(battery.needs_service(wear_tires))
