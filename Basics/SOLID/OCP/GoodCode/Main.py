from Basics.OOPS import DebitCard
from Basics.UML.Realization import CreditCardPayment
from BehavourialPatterns.SOLID.OCP.BadCode import PaymentProcessor


if __name__ == "__main__":
    PayementProcessor = PaymentProcessor()
    credit_card_payment = CreditCardPayment("1234-5678-9012-3456", "12/25", "123")
    debit_card_payment = DebitCard("9876-5432-1098-7654", "11/24", "456")
    
    PayementProcessor.pay(credit_card_payment, 100)
    PayementProcessor.pay(debit_card_payment, 200)

    

    