from Basics.OOPS import PaymentMethod


class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paid using PayPal of amount: {amount}")