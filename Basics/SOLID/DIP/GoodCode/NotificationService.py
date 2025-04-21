from NotificationChannel import NotificationChannel


class NotificationService:
    def __init__(self, notificationchannel: NotificationChannel):
        self.notificationchannel = notificationchannel

    def send(self, message):
        self.notificationchannel.send(message)