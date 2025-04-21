from PizzaDecorator import PizzaDecorator
from Pizza import Pizza

class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

    def get_description(self) -> str:
        return super().get_description() + ", Cheese"

    def get_cost(self) -> float:
        return super().get_cost() + 1.50