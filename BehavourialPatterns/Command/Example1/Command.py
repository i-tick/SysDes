from abc import ABC, abstractmethod

# Command Interface

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Concrete Classes for Commands
class BoldCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.bold_text()

class ChangeColorCommand(Command):
    def __init__(self, editor):
        self.editor = editor

    def execute(self):
        self.editor.change_color()

# Button Class
class Button:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def click(self):
        if self.command:
            self.command.execute()

# Receiver: TextEditor class
class TextEditor:
    def bold_text(self):
        print("Text has been bolded.")

    def italicize_text(self):
        print("Text has been italicized.")

    def underline_text(self):
        print("Text has been underlined.")

    def change_color(self):
        print("Text color has been changed.")

# Main function
if __name__ == "__main__":
    editor = TextEditor()

    # Button
    # Decoupling -> One button can do many types of actions, decoupled from the text editor!
    button = Button()
    button.set_command(BoldCommand(editor))
    button.click()

    button.set_command(ChangeColorCommand(editor))
    button.click()