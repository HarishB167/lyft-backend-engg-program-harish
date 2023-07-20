from tire.tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, test_results) -> None:
        self.test_results = test_results

    def needs_service(self):
        if sum(self.test_results) >= 3:
            return True
        return False
