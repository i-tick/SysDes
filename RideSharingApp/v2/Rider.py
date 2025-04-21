from User import User

class rider(User):
    def __init__(self, name, email, location):
        super().__init__(name, email, location)
        
    
    def notify(self, message: str) -> None:
        print(f"Notification for rider {self.name}: {message}")