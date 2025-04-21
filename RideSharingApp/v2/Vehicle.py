from abc import ABC, abstractmethod
class Vehicle:
    def __init__(self, numberplate: str):
        self.numberplate = numberplate

    @abstractmethod
    def priceperkm(self) -> float:
        """Return the price per kilometer for the vehicle."""
        pass