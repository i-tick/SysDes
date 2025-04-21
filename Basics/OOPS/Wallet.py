import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Basics.OOPS.PaymentMethod import PaymentMethod

class Wallet(PaymentMethod):
    
    def pay(self):
        print("Payment made using Wallet")