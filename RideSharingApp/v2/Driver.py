from User import User
from Vehicle import Vehicle
from Location import location
class driver(User):
    def __init__(self, name, email, location: location, vehicle: Vehicle):
        super().__init__(name, email, location)
        self.vehicle = vehicle

    def get_vehicle(self) -> Vehicle:
        return self.vehicle
    
    def notify(self, message):
        print(f"Notification for driver {self.name}: {message}")
    
    