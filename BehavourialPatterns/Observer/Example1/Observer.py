from abc import ABC, abstractmethod
class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, temp: float) -> None:
        pass

class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class WeatherStation(Subject):
    """
    The WeatherStation class implements the Subject interface. It maintains a list
    of observers and notifies them of any state changes.
    """
    def __init__(self):
        self._observers = []
        self._temperature = 0.0

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, temperature: float) -> None:
        self._temperature = temperature
        self.notify()

class DisplayDevice(Observer):
    """
    The DisplayDevice class implements the Observer interface to display temperature
    updates.
    """
    def __init__(self,name):
        self.name = name
    def update(self, temp: float) -> None:
        print(f"Current Temperature: {temp} °C in device {self.name}")

class MobileApp(Observer):
    """
    The MobileApp class implements the Observer interface to receive temperature
    updates on a mobile app.
    """
    def update(self, temp: float) -> None:
        print(f"Mobile App: Current Temperature: {temp} °C")


if __name__ == "__main__":
    # Example usage
    weather_station = WeatherStation()
    
    # Assuming DisplayDevice is a concrete implementation of Observer
    display_device = DisplayDevice("Living Room")
    mobile_app = MobileApp()
    
    weather_station.attach(display_device)
    weather_station.attach(mobile_app)
    
    weather_station.set_temperature(25.0)

    
    weather_station.detach(display_device)
    weather_station.set_temperature(30.0)