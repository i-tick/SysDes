from abc import ABC, abstractmethod

class ChatMediator(ABC):
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """
    @abstractmethod
    def send(self, message: str, users: 'User') -> None:
        pass
    def add_user(self, user: 'User') -> None:
        pass

class User:
    """
    The User class contains a reference to the mediator and communicates with
    it whenever it wants to send a message.
    """
    def __init__(self, name: str, mediator: ChatMediator) -> None:
        self._name = name
        self._mediator = mediator

    def get_name(self) -> str:
        return self._name

    def send(self, message: str) -> None:
        print(f"{self._name} sends: {message}")
        self._mediator.send(message, self)

    def receive(self, message: str, sender: 'User') -> None:
        print(f"{self._name} received: {message} from {sender.get_name()}")

class ChatRoom(ChatMediator):
    """
    The ChatRoom class implements the ChatMediator interface and coordinates
    communication between different users.
    """
    def __init__(self) -> None:
        self._users = []

    def add_user(self, user: User) -> None:
        self._users.append(user)

    def send(self, message: str, sender: User) -> None:
        for user in self._users:
            if user != sender:
                user.receive(message,sender)

if __name__ == "__main__":
    ChatRoom = ChatRoom()

    user1 = User("Alice", ChatRoom)
    user2 = User("Bob", ChatRoom)
    user3 = User("Charlie", ChatRoom)

    ChatRoom.add_user(user1)
    ChatRoom.add_user(user2)
    ChatRoom.add_user(user3)

    user1.send("Hello, Everyone!")

