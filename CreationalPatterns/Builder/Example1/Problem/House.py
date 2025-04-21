class House:
    def __init__(self, walls: int, roof: str, windows: int, doors: int,
                 garage: str=None, garden: str=None, swimming_pool: str=None):
        self._walls = walls
        self._roof = roof
        self._windows = windows
        self._doors = doors
        self._garage = garage
        self._garden = garden
        self._swimming_pool = swimming_pool

    def __str__(self):
        return f"House with {self._walls} walls, {self._roof} roof, {self._windows} windows, " \
               f"{self._doors} doors, {self._garage} garage, {self._garden} garden, " \
               f"{self._swimming_pool} swimming pool"
    def set_garage(self, garage):
        self._garage = garage

    def set_garden(self, garden: str):
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
    house = House(2, "sloped", 10, 2, "attached", "front yard", "in-ground")
    # // Constructor Explosion -> Too Many Constructors
    # // Difficult to understand and maintain this code
    # // this is where builder pattern comes into picture

    # 1. if too many parameters
    # 2. if we want to validate the parameters
    # 3. if the class is immutable
    # 4 validation may involve multiple parameters
    # 5. if we want to create different variations of the class
    
    print(house)