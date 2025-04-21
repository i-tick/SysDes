from NotificationChannel import NotificationChannel


class SMSService(NotificationChannel):
    def send(self, message):
        # Logic to send SMS
        print(f"Sending SMS: {message}")