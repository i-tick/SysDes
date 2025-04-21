from GoodCode.PaymentMethod import PaymentMethod


class CreditCard(PaymentMethod):

    def pay(self, amount):
        print(f"Paid using Credit Card of amount: {amount}")