from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str) -> None:
        """Send a notification."""
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self, message: str) -> None:
        print(f"Sending email notification: {message}")

class SendGridNotificationService():
    def send_grid_notification(self, message: str) -> None:
        print(f"Sending SendGrid notification: {message}")

class SendGridAdapter(NotificationService):
    def __init__(self, sendgrid_service: SendGridNotificationService) -> None:
        self.sendgrid_service = sendgrid_service

    def send_notification(self, message: str) -> None:
        self.sendgrid_service.send_grid_notification(message)

if __name__ == "__main__":
    # Example usage
    email_service = EmailNotificationService()
    email_service.send_notification("Hello, this is an email notification!")

    sendgrid_service = SendGridNotificationService()
    # sendgrid_service.send_notification("Hello, this is a SendGrid notification!")
    # This will raise an error because the method does not exist


    SendGridAdapter(sendgrid_service).send_notification("Hello, this is a SendGrid notification!")
    # This will work because we are using the adapter
    # The adapter translates the method call to the correct method in the SendGrid service
    # This is the main difference between the two
    # The adapter allows us to use the SendGrid service as if it were a NotificationService
    # without modifying the SendGrid service itself


    