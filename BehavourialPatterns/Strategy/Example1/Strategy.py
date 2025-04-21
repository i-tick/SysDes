from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self):
        pass

# Concrete Strategy: Credit Card
class CreditCardPayment(PaymentStrategy):
    def process_payment(self):
        print("Making payment via Credit Card")

# Concrete Strategy: Debit Card
class DebitCardPayment(PaymentStrategy):
    def process_payment(self):
        print("Making payment via Debit Card")

# Concrete Strategy: UPI
class UPIPayment(PaymentStrategy):
    def process_payment(self):
        print("Making payment via UPI")

# Context Class
class PaymentService:
    def __init__(self):
        self.strategy = None

    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def pay(self):
        if self.strategy:
            self.strategy.process_payment()
        else:
            print("No payment strategy set")

# Client Code
if __name__ == "__main__":
    payment_service = PaymentService()
    payment_service.set_payment_strategy(UPIPayment())
    payment_service.pay()