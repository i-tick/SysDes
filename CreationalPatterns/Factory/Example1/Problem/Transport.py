from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        """Deliver the product."""
        pass

class Truck(Transport):
    def deliver(self) -> str:
        return "Delivering by land in a box."
class Ship(Transport):
    def deliver(self) -> str:
        return "Delivering by sea in a container."
class Airplane(Transport):
    def deliver(self) -> str:
        return "Delivering by air in a cargo plane."
    
# Transport Service
# It is tightly coupled with the Transport class
# Adding a new transport type requires modifying the service class
# This violates the Open/Closed Principle
if __name__ == "__main__":
    # Example usage
    truck = Truck()
    print(truck.deliver())  # Output: Delivering by land in a box.
    
    ship = Ship()
    print(ship.deliver())  # Output: Delivering by sea in a container.
    
    airplane = Airplane()
    print(airplane.deliver())  # Output: Delivering by air in a cargo plane.