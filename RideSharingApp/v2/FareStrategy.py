from abc import ABC, abstractmethod
from Vehicle import Vehicle
class FareStrategy(ABC):
    """
    The base class for all fare strategies. This class defines the interface for
    calculating fares.
    """

    @abstractmethod
    def calculate_fare(self, vehicle: Vehicle, distance: float) -> float:
       pass

class StandardFareStrategy(FareStrategy):
    """
    A standard fare strategy that calculates the fare based on a fixed rate per km.
    """

    def calculate_fare(self, vehicle: Vehicle, distance: float) -> float:
        return vehicle.priceperkm() * distance

class SharedFareStrategy(FareStrategy):
    """
    A shared fare strategy that calculates the fare based on a fixed rate per km
    and a shared discount.
    """

    def calculate_fare(self, vehicle: Vehicle, distance: float) -> float:
        return (vehicle.priceperkm() * distance) * 0.8  # 20% discount for shared rides
    
class LuxuryFareStrategy(FareStrategy):
    """
    A luxury fare strategy that calculates the fare based on a fixed rate per km
    and a premium surcharge.
    """

    def calculate_fare(self, vehicle: Vehicle, distance: float) -> float:
        return (vehicle.priceperkm() * distance) + 50  # 50 currency units surcharge for premium rides