from GoodCode.PaymentMethod import PaymentMethod


class DebitCard(PaymentMethod):

    def pay(self, amount):
        print(f"Paid using Debit Card of amount: {amount}")