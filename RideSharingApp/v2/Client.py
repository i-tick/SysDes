from RideMatching import RideMatching
from Rider import rider
from FareStrategy import StandardFareStrategy, SharedFareStrategy, LuxuryFareStrategy

from Driver import driver
from Location import location
from Car import Car
from Bike import Bike
if __name__ == "__main__":
    # Example usage
    ride_matching = RideMatching()

    
    # Add drivers to the ride matching system
    driver1 = driver("Driver1", "driver1@gmail.com", location(10, 20), Car("AB1234"))
    driver2 = driver("Driver2", "driver2@gmail.com",location(30, 40), Bike("XY5678"))
    ride_matching.add_drivers(driver1)
    ride_matching.add_drivers(driver2)
    
    # Create a rider and match with a driver
    rider = rider("Rider1", "rider1@gmail.com",location(15, 25))
    fare_strategy = StandardFareStrategy()
    ride_matching.match_driver(rider, 10, fare_strategy)