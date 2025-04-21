from abc import ABC, abstractmethod

class Checkbox(ABC):
    @abstractmethod
    def checkbox(self) -> str:
        """Render the checkbox."""
        pass

class MacCheckbox(Checkbox):
    def checkbox(self) -> str:
        return "Mac Checkbox"

class WindowsCheckbox(Checkbox):
    def checkbox(self) -> str:
        return "Windows Checkbox"
