from abc import ABC, abstractmethod

# Payment interface (Realization)
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Class implementing the Payment interface
class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f"Paid ${amount} using credit card.")

# Main function
if __name__ == "__main__":
    payment: Payment = CreditCardPayment()
    payment.pay(100.0)  # Output: Paid $100.0 using credit card.