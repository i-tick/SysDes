from Pizza import Pizza

class BasicPizza(Pizza):
    def get_description(self) -> str:
        return "Basic Pizza"
    def get_cost(self) -> float:
        return 5.00