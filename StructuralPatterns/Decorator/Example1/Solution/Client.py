 
from BasicPizza import BasicPizza
from CheeseDecorator import CheeseDecorator
from OlivesDecorator import OlivesDecorator
if __name__ == "__main__":
    # Example usage
    pizza = BasicPizza()
    print(f"Description: {pizza.get_description()}")
    print(f"Cost: ${pizza.get_cost():.2f}")

    pizza = CheeseDecorator(pizza)
    print(f"\nDescription: {pizza.get_description()}")
    print(f"Cost: ${pizza.get_cost():.2f}")

    pizza = OlivesDecorator(pizza)
    print(f"\nDescription: {pizza.get_description()}")
    print(f"Cost: ${pizza.get_cost():.2f}")

    # Flexibility: You can add new toppings without modifying existing code.
    # Scalability: You can easily add new decorators for different toppings.
    # Maintainability: Each decorator is a separate class, making it easier to manage.
    # Single Responsibility Principle: Each class has a single responsibility.
    # Open/Closed Principle: You can extend the functionality of the pizza without modifying existing code.
    # Dynamic Behavior: You can change the behavior of the pizza at runtime by adding or removing decorators.
    # Combination of Behaviors: You can combine multiple decorators to create complex behaviors.