class location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def get_latitude(self):
        return self.latitude
    def get_longitude(self):
        return self.longitude
    
    def calc_distance(self, other_location):
        dx = self.latitude - other_location.get_latitude()
        dy = self.longitude - other_location.get_longitude()
        return (dx**2 + dy**2)**0.5
