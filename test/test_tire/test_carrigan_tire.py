import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):

    def test_tire_should_be_serviced(self):
        test_results = [0.8, 0.8, 0.8, 0.9]

        engine = CarriganTire(test_results)
        self.assertTrue(engine.needs_service())

    def test_tire_should_not_be_serviced(self):
        test_results = [0.8, 0.8, 0.8, 0.8]

        engine = CarriganTire(test_results)
        self.assertFalse(engine.needs_service())
