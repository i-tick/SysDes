from enum import Enum
class RideStatus(Enum):
    SCHEDULED = "Scheduled"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
from Rider import rider
from Driver import driver
from FareStrategy import FareStrategy
from enum import Enum
class Ride:
    def __init__(self, rider: rider, driver: driver, fare_strategy: FareStrategy, distance: float):
        self.rider = rider
        self.driver = driver
        self.fare_strategy = fare_strategy
        self.distance = distance
        self.status = RideStatus.SCHEDULED

    def calculate_fare(self):
        self.fare = self.fare_strategy.calculate_fare(self.driver.get_vehicle(), self.distance)
        
    def update_status(self, status: RideStatus) -> None:
        self.status = status
        self.notify_rider_and_driver(status)
    
    def notify_rider_and_driver(self, status: RideStatus) -> None:
        self.rider.notify(f"Ride status updated to: {status.value}")
        self.driver.notify(f"Ride status updated to: {status.value}")

    def get_fare(self) -> float:
        return self.fare