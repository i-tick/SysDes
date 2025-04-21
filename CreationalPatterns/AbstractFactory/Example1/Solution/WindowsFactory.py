from UIFactory import UIFactory
from Button import Button, WindowsButton
from Checkbox import Checkbox, WindowsCheckbox

class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()