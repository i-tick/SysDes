class MacButton:
    def paint(self):
        print("Mac Button")
class MacCheckbox:
    def checkbox(self):
        print("Mac Checkbox")
class WindowsButton:
    def paint(self):
        print("Windows Button")
class WindowsCheckbox:
    def checkbox(self):
        print("Windows Checkbox")

class Application:
    # Tight coupling
    # Not flexible
    # Not easy to extend
    # Not easy to maintain
    # Not easy to test
    # Not easy to change
    WindowsButton = WindowsButton()
    WindowsCheckbox = WindowsCheckbox()
    WindowsButton.paint()
    WindowsCheckbox.checkbox()