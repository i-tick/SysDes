class PaymentProcessor:
    def process_payment(self, payment_method: str, amount: float):
        if payment_method == "CreditCard":
            # Business logic
            print(f"Making payment via Credit Card: {amount}")
        elif payment_method == "DebitCard":
            # Business logic
            print(f"Making payment via Debit Card: {amount}")
        elif payment_method == "Paypal":
            # Business logic
            print(f"Making payment via PayPal: {amount}")
        else:
            raise ValueError(f"Unsupported payment method: {payment_method}")