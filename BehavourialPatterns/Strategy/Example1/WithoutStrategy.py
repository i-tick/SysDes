class PaymentService:
    def process_payment(self, payment_method):
        if payment_method == "Credit Card":
            print("Making payment via credit card")
        elif payment_method == "Debit Card":
            print("Making payment via debit card")
        elif payment_method == "UPI":
            # huge algorithm
            print("Making payment via UPI")
        else:
            print("Unsupported Payment method")


if __name__ == "__main__":
    payment_service = PaymentService()
    payment_service.process_payment("UPI")