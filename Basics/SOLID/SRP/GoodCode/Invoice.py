class Invoice:
    def __init__(self, amount):
        self.amount = amount

    # Additional Functionality
    def generate_invoice(self):
        print(f"Invoice generated & printed for amount {self.amount}")