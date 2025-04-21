class User:
    def __init__(self, name):
        self.__name = name

    def send(self, message, recipient):
        print(f"{self.__name} sends: {message} to {recipient.get_name()}")
    
    def get_name(self):
        return self.__name
        

if __name__ == "__main__":
    user1 = User("Alice")
    user2 = User("Bob")
    user3 = User("Charlie")
    
    user1.send("Hello, Bob!", user2)
    user2.send("Hi, Alice!", user1)
    user3.send("Hey, everyone!", user1)