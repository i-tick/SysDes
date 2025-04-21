from Vehicle import Vehicle
class Bike(Vehicle):
    def __init__(self, numerplate):
        super().__init__(numerplate)

    def priceperkm(self) -> float:
        """Calculate the fare for a km"""
        fare = 5.0
        return fare