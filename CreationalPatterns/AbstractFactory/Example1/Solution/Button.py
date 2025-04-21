from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self) -> str:
        """Render the button."""
        pass


class MacButton(Button):
    def paint(self) -> str:
        return "Mac Button"
    
class WindowsButton(Button):
    def paint(self) -> str:
        return "Windows Button"