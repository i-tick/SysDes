class Invoice:
    def __init__(self, amount):
        self.amount = amount

    # Additional Functionality
    def generate_invoice(self):
        print(f"Invoice generated & printed for amount {self.amount}")

    def save_to_database(self):
        print("Saving invoice to Database")

    def send_email_notification(self):
        print("Sending email notification for invoice")