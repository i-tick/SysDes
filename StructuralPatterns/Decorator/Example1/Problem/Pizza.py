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

class BasicPizza(Pizza):
    def get_description(self) -> str:
        return "Basic Pizza"
    def get_cost(self) -> float:
        return 5.00

class CheesePizza(BasicPizza):
    def get_description(self) -> str:
        return super().get_description() + ", Cheese"
    def get_cost(self) -> float:
        return super().get_cost() + 1.50
    
class CheeseOlivesPizza(CheesePizza):
    def get_description(self) -> str:
        return super().get_description() + ", Olives"
    def get_cost(self) -> float:
        return super().get_cost() + 0.75
    
if __name__ == "__main__":
    # Example usage


    cheese_olives_pizza = CheeseOlivesPizza()
    print(f"\nDescription: {cheese_olives_pizza.get_description()}")
    print(f"Cost: ${cheese_olives_pizza.get_cost():.2f}")
    # Problem: Scalability, Difficult to maintain, and Lack of flexibility, difficult to test
    # Solution: Use the decorator pattern to add new functionality to the pizza class