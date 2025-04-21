import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Basics.OOPS.PaymentMethod import PaymentMethod

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id
    def pay(self):
        print("Payment made using UPI")