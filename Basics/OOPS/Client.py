import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Basics.OOPS.Wallet import Wallet
from Basics.OOPS.PaymentService import PaymentService
from Basics.OOPS.CreditCard import CreditCard
from Basics.OOPS.DebitCard import DebitCard
from Basics.OOPS.UPI import UPI


class Client:  # Client class


    def run(self):
        paymentService = PaymentService()
        paymentService.add_payment_method("Aitik Debit Card", DebitCard("1234-5678-9101-1121", "Aitik Dandapat"))
        paymentService.add_payment_method("Aitik Credit Card", CreditCard("1121-2345-6789-0123", "Aitik Dandapat"))
        paymentService.add_payment_method("Aitik UPI", UPI("aitik@upi"))
        paymentService.add_payment_method("Aitik Wallet", Wallet())  

        paymentService.make_payment("Aitik Debit Card")
        paymentService.make_payment("Aitik Credit Card")
        paymentService.make_payment("Aitik UPI")
        paymentService.make_payment("Aitik Wallet")
if __name__ == "__main__":
    client = Client()
    client.run()