from abc import ABC, abstractmethod
from Location import location
class User(ABC):
    def __init__(self, name, email, location: location):
        self.name = name
        self.email = email
        self.location = location

    def get_location(self) -> location:
        return self.location
    
    def get_name(self) -> str:
        return self.name
    
    def set_location(self, location: location) -> None:
        self.location = location

    @abstractmethod
    def notify(self, message: str) -> None:
        """Notify the user with a message."""
        pass

   