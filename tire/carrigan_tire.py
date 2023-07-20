from tire.tire import Tire


class CarriganTire(Tire):

    def __init__(self, test_results) -> None:
        self.test_results = test_results

    def needs_service(self):
        for result in self.test_results:
            if result >= 0.9:
                return True
        return False
