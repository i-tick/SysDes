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


if __name__ == "__main__":
    # Example usage
    email_service = EmailNotificationService()
    email_service.send_notification("Hello, this is an email notification!")

    sendgrid_service = SendGridNotificationService()
    # sendgrid_service.send_notification("Hello, this is a SendGrid notification!")
    # This will raise an error because the method does not exist
    # It is tightly coupled with SednGridNotificationService

    # Problems
    # 1. cant allow Plug and Play
    # 2. connection to 3rd party apps
    # 3. library might be deprecated
    # 4. another type of connection

  