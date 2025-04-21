class HouseBuilder:
    def __init__(self, walls, roof, windows, doors):
        self._walls = walls
        self._roof = roof
        self._windows = windows
        self._doors = doors
        self._garage = None
        self._garden = None
        self._swimming_pool = None

    def set_walls(self, walls):
        self._walls = walls
        return self
    def set_roof(self, roof):
        self._roof = roof
        return self
    def set_windows(self, windows):
        self._windows = windows
        return self
    def set_doors(self, doors):
        self._doors = doors
        return self

    def set_garage(self, garage):
        self._garage = garage
        return self

    def set_garden(self, garden):
        self._garden = garden
        return self

    def set_swimming_pool(self, swimming_pool):
        self._swimming_pool = swimming_pool
        return self

    def build(self):
        return House(self)
class House:
    def __init__(self, builder):
        self._walls = builder._walls
        self._roof = builder._roof
        self._windows = builder._windows
        self._doors = builder._doors
        self._garage = builder._garage
        self._garden = builder._garden
        self._swimming_pool = builder._swimming_pool
        
    def __str__(self):
        return f"House with {self._walls} walls, {self._roof} roof, {self._windows} windows, " \
               f"{self._doors} doors, {self._garage} garage, {self._garden} garden, " \
               f"{self._swimming_pool} swimming pool"
    
    def builder(walls,roof, windows, doors):
        return HouseBuilder(walls,roof, windows, doors)
    
    def set_garage(self, garage):
        self._garage = garage

    def set_garden(self, garden):
        self._garden = garden

    def set_swimming_pool(self, swimming_pool):
        self._swimming_pool = swimming_pool

    def set_walls(self, walls):
        self._walls = walls

    def set_roof(self, roof):
        self._roof = roof

    def set_windows(self, windows):
        self._windows = windows

    def set_doors(self, doors):
        self._doors = doors


if __name__ == "__main__":
    house = House.builder(2,"sloped", 10, 2).set_garage("attached").build()

    
    print(house)