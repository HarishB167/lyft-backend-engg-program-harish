import unittest
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        test_results = [1, 1, 1, 0]

        engine = OctoprimeTire(test_results)
        self.assertTrue(engine.needs_service())

    def test_tire_should_not_be_serviced(self):
        test_results = [1, 1, 0, 0]

        engine = OctoprimeTire(test_results)
        self.assertFalse(engine.needs_service())
