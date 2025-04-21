from UIFactory import UIFactory
from Button import Button, MacButton
from Checkbox import Checkbox, MacCheckbox

class MacFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()