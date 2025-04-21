from abc import ABC, abstractmethod

class TransportMode(ABC):
    """
    The TransportMode interface declares a method for executing a trip.
    """
    @abstractmethod
    def get_eta(self) -> int:
        """
        Returns the estimated time of arrival for the trip.
        """
        pass
    @abstractmethod
    def get_direction(self) -> str:
        """
        Returns the directions for the trip.
        """
        pass

class Cycle(TransportMode):
    """
    The Cycle class implements the TransportMode interface for cycling.
    """
    def get_eta(self):
        print("Calc ETA for cycling 5")
        return 5
    def get_direction(self):
        return "Directions for cycling: Take the bike lane on Elm Street."
    
class Walk(TransportMode):
    """
    The Walk class implements the TransportMode interface for walking.
    """
    def get_eta(self):
        print("Calc ETA for walking 10")
        return 10
    def get_direction(self):
        return "Directions for walking: Head north for 500 meters."
class Car(TransportMode):
    """
    The Car class implements the TransportMode interface for driving.
    """
    def get_eta(self):
        print("Calc ETA for car 2")
        return 2
    def get_direction(self):
        return "Directions for driving: Use highway 50 towards downtown."
class Train(TransportMode):
    """
    The Train class implements the TransportMode interface for train travel.
    """
    def get_eta(self):
        print("Calc ETA for train 3")
        return 3
    def get_direction(self):
        return "Directions for train: Board the Red Line at Central Station."
class DirectionService:
    """
    The DirectionService class maintains a reference to the current transport mode
    and delegates the trip execution to it.
    """
    def __init__(self, mode: TransportMode):
        self.mode = mode

    def set_mode(self, mode: TransportMode) -> None:
        self.mode = mode

    def getETA(self):
        return self.mode.get_eta()
    def getDirection(self) -> str:
        return self.mode.get_direction()
    

if __name__ == "__main__":
    # Create a DirectionService instance with an initial mode
    service = DirectionService(Cycle())
    
    # Get ETA and directions for the current mode
    print(service.getETA())
    print(service.getDirection())
    
    # Change the transport mode to walking
    service.set_mode(Walk())
    
    # Get ETA and directions for the new mode
    print(service.getETA())
    print(service.getDirection())