class PayementProcessor:

    def process_payment(self, payment_method, amount):
        payment_method.pay(amount)