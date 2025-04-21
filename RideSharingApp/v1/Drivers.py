class drivers:
    def __init__(self, name, vehicle, location):
        self.name = name
        self.vehicle = vehicle
        self.location = location

    def get_location(self):
        return self.location
    
    def set_location(self, location):
        self.location = location
        print(f"{self.name}'s new location is {self.location}.")
    