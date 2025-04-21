from abc import ABC, abstractmethod
from WindowsFactory import WindowsFactory
from MACFactory import MacFactory
    
class Application:
    def __init__(self, factory):
        self._factory = factory
        self._button = None
        self._checkbox = None

    def create_ui(self):
        self._button = self._factory.create_button()
        self._checkbox = self._factory.create_checkbox()

    def render(self):
        print(self._button.paint())
        print(self._checkbox.checkbox())

if __name__ == "__main__":
    # Example usage
    factory = WindowsFactory()  # Change to MacFactory() for Mac UI
    app = Application(factory)
    app.create_ui()
    app.render()