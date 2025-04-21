
from RideSharingAppService import RideSharingAppService
from Drivers import drivers
from Riders import riders
from Location import location
from Vehicle import vehicle


if __name__ == "__main__":
    app = RideSharingAppService()
    
    # Create drivers and riders
    driver1 = drivers("John", vehicle("JH12345", "bike"), location(10, 20))
    driver2 = drivers("Alice", vehicle("OD12345", "car"), location(15, 25))
    rider1 = riders("Bob", location(12, 22))
    rider2 = riders("Charlie", location(18, 28))
    
    # Add drivers and riders to the system
    app.add_driver(driver1)
    app.add_driver(driver2)
    app.add_rider(rider1)
    app.add_rider(rider2)
    
    # Request rides
    print('\n')
    app.request_ride(rider1, 5)
    print("\n")
    app.request_ride(rider2, 10)


    # SRP IS VIOLATED: THIS RideSharingAppService DOES EVERYTHING
    # OCP IS VIOLATED: THIS RideSharingAppService IS NOT OPEN FOR EXTENSION (CALC_FARE IS HARDCODED)
    # LSP IS VIOLATED: bIKE, CAR CLASS IS NOT A SUBCLASS OF VEHICLE
    # ISP IS VIOLATED: THIS RideSharingAppService IS NOT INTERFACE SEGREGATED
    # DIP IS VIOLATED: THIS RideSharingAppService DEPENDS ON HIGH LEVEL MODULES (RideSharingAppService) AND LOW LEVEL MODULES (CALC_FARE)
    