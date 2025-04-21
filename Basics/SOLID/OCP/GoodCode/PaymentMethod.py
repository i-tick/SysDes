from abc import ABC,abstractmethod

# PaymentMethod class
# This class defines the interface for payment methods
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass