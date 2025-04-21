from Basics.OOPS import PaymentMethod


class UPI(PaymentMethod):

    def pay(self, amount):
        print("Payment made using UPI of amount: ", amount)