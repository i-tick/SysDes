import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Basics.OOPS import PaymentMethod


class PaymentService:
    def __init__(self):
        self.payment_methods = {}

    def add_payment_method(self, name, payment_method: PaymentMethod):
        self.payment_methods[name] = payment_method

    def make_payment(self, name):
        payment_method = self.payment_methods[name]
        payment_method.pay()