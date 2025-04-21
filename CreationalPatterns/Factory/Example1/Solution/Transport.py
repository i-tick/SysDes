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

class TransportFactory:
    @staticmethod
    def create_transport(transport_type: str) -> Transport:
        if transport_type == "truck":
            return Truck()
        elif transport_type == "ship":
            return Ship()
        elif transport_type == "airplane":
            return Airplane()
        else:
            raise ValueError(f"Unknown transport type: {transport_type}")
    
if __name__ == "__main__":
    # Example usage
    transport_type = "truck"  # This can be changed to "ship" or "airplane"
    transport = TransportFactory.create_transport(transport_type)
    print(transport.deliver())  # Output: Delivering by land in a box.

    # it moves the transport creation logic to a separate factory class
    # This allows for easy extension of transport types without modifying the existing code
    # OCP is followed

    # CREATE CORRESPONDING SUBCLASS BASED ON CONDITION

    # Usecase:
    # 1. Transport Factory: The factory creates different transport objects based on the input type.
    # 2. UI ELEMENTS BASED ON OS: The factory creates different UI elements based on the operating system.
    # 3. DATABASE CONNECTION: The factory creates different database connection objects based on the database type.
    # 4. PAYMENT GATEWAY: The factory creates different payment gateway objects based on the payment method.


    # IF TOO MANE FACTORY CLASS THEN USE ABSTRACT FACTORY
    # 1. Abstract Factory: The abstract factory creates families of related or dependent objects without specifying their concrete classes.
