from abc import ABC, abstractmethod
from Button import Button
from Checkbox import Checkbox
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        """Create a button."""
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """Create a checkbox."""
        pass
