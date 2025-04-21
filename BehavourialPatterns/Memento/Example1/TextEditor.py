from TextEditorMemento import TextEditorMemento


class TextEditor:
    def __init__(self):
        self.text = ''

    def write(self, text: str):
        self.text += text

    def get_text(self):
        return self.text

    def save(self):
        return TextEditorMemento(self.text)

    def restore(self, memento):
        if memento is None:
            self.text = ''
            return
        self.text = memento.get_text()