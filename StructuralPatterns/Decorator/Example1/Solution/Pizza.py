from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        """Get the description of the pizza."""
        pass

    @abstractmethod
    def get_cost(self) -> float:
        """Get the cost of the pizza."""
        pass

   