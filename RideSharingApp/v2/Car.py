from Vehicle import Vehicle
class Car(Vehicle):
    def __init__(self, numerplate):
        super().__init__(numerplate)

    def priceperkm(self) -> float:
        """Calculate the fare for a km"""
        fare = 10.0
        return fare