from abc import ABC, abstractmethod
from Pizza import Pizza

class PizzaDecorator(Pizza, ABC):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        return self._pizza.get_description()

    @abstractmethod
    def get_cost(self) -> float:
        return self._pizza.get_cost()