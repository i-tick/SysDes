class TextEditor:
    def bold_text(self):
        print("Text has been bolded.")

    def italicize_text(self):
        print("Text has been italicized.")

    def underline_text(self):
        print("Text has been underlined.")


# UI Button Classes
class BoldButton:
    def __init__(self, editor):
        self.editor = editor

    def click(self):
        self.editor.bold_text()


class ItalicButton:
    def __init__(self, editor):
        self.editor = editor

    def click(self):
        self.editor.italicize_text()


if __name__ == "__main__":
    editor = TextEditor()
    bold_button = BoldButton(editor)
    italic_button = ItalicButton(editor)
    bold_button.click()
    italic_button.click()