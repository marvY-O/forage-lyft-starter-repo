import unittest

from Tires.OctoprimeTires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        wear_tires = [0.4, 0.9, 1.0, 0.9]
        battery = OctoprimeTires(wear_tires)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        wear_tires = [0.8, 0.5, 0.4, 0.8]
        battery = OctoprimeTires(wear_tires)
        self.assertTrue(battery.needs_service())
