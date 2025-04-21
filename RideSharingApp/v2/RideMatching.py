from Rider import rider
from Ride import Ride, RideStatus
from FareStrategy import FareStrategy

from Driver import driver

class RideMatching:
    def __init__(self):
        self.drivers = []

    def add_drivers(self, driver: driver) -> None:
        self.drivers.append(driver)

    def match_driver(self, rider: rider, distance: float, fare_strategy: FareStrategy) -> None:
        if not self.drivers:
            rider.notify("No drivers available")
            return None
        nearest_driver = self.find_nearest_driver(rider.get_location())

        self.drivers.remove(nearest_driver)
        rider.notify(f"Driver {nearest_driver.get_name()} is on the way")

        ride = Ride(rider, nearest_driver, fare_strategy, distance)
        ride.calculate_fare()
        rider.notify(f"Ride booked with driver {nearest_driver.get_name()}. Fare: {ride.get_fare()}")
        nearest_driver.notify(f"Ride booked with rider {rider.get_name()}. Fare: {ride.get_fare()}")

        ride.update_status(RideStatus.ONGOING)

        # Simulate ride completion
        ride.update_status(RideStatus.COMPLETED)
        self.drivers.append(nearest_driver)  # Re-add the driver to the pool after the ride is completed
        

    def find_nearest_driver(self, rider_location):
        driver_assigned = None
        min_distance = float('inf')
        for driver in self.drivers:
            driver_distance = rider_location.calc_distance(driver.get_location())
            if driver_distance < min_distance:
                driver_assigned = driver
                min_distance = driver_distance
        return driver_assigned