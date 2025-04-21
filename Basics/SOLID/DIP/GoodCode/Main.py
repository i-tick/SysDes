from EmailService import EmailService
from SMSService import SMSService
from NotificationService import NotificationService


if __name__ == "__main__":
    email_service = NotificationService(EmailService())
    sms_service = NotificationService(SMSService())

    email_service.send("Hello via Email!")
    sms_service.send("Hello via SMS!")