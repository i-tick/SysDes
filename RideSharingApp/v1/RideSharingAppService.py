class RideSharingAppService:
    
    def __init__(self):
        self.drivers = []
        self.riders = []
        

    def add_driver(self, driver):
        self.drivers.append(driver)
        print(f"Driver {driver.name} added to the system.")
    def add_rider(self, rider):
        self.riders.append(rider)
        print(f"Rider {rider.name} added to the system.")
        
    def request_ride(self, rider, distance):
        if not self.drivers:
            print("No drivers available.")
            return
        driver_assigned = None
        mind = float('inf')
        for driver in self.drivers:
            curdis = self._calculate_distance(driver.location, rider.location)
            if curdis < mind:
                mind = curdis
                driver_assigned = driver

        # Fare calculation
        expexted_fair = self._calculate_fare(driver_assigned.vehicle, distance)

        # Show driver details
        print(f"Driver {driver_assigned.name} is assigned to rider {rider.name}.")
        print(f"Expected fare for the ride is {expexted_fair}.")

    def _calculate_fare(self,vehicle, distance):
        if vehicle == "car":
            fare = distance * 10
        elif vehicle == "bike":
            fare = distance * 5
        else:
            fare = distance * 15
        return fare
    
    def _calculate_distance(self,location1, location2):
        # Dummy distance calculation
        dx = location1.get_latitude() - location2.get_latitude()
        dy = location1.get_longitude() - location2.get_longitude()
        return (dx**2 + dy**2)**0.5