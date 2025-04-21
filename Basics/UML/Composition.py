class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine started with {self.horsepower} HP.")


class Wheel:
    def __init__(self, type):
        self.type = type
    
    def rotate(self):
        print(f"The {self.type} wheel is rotating.")


class Transmission:
    def __init__(self, type):
        self.type = type
    
    def shift_gear(self):
        print(f"Transmission shifted: {self.type}")


class Car:
    def __init__(self):
        self.engine = Engine(150)
        self.wheel = Wheel("Alloy")
        self.transmission =  Transmission("Automatic")
    
    def drive(self):
        self.engine.start()
        self.wheel.rotate()
        self.transmission.shift_gear()
        print("Car is moving!")


# Example Usage
if __name__ == "__main__":
    
    
    car = Car()
    car.drive()