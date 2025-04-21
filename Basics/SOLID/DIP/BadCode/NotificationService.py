from BadCode import EmailService, SMSService


class EmailNotification:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def sendemail(self,message):
        self.email_service.send_email(message)
        
    def sendsms(self,message):
        self.sms_service.send_sms(message)