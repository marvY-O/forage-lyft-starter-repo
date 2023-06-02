import unittest

from test_battery.test_nubbin_battery import TestNubbinBattery
from test_battery.test_spindler_battery import TestSpindlerBattery

from test_engine.test_capulet_engine import TestCapuletEngine
from test_engine.test_sternman_engine import TestSternmanEngine
from test_engine.test_willoughby_engine import TestWilloughbyEngine

from test_tire.test_carrigan_tires import CarriganTires
from test_tire.test_octoprime_tires import OctoprimeTires


def run_some_tests():
    # Run only the tests in the specified classes

    test_classes_to_run = [TestNubbinBattery, TestSpindlerBattery, TestCapuletEngine, TestSternmanEngine, TestWilloughbyEngine, CarriganTires, OctoprimeTires]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
        
    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)

    

if __name__ == '__main__':
    run_some_tests()

