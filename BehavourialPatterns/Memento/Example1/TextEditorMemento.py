class TextEditorMemento:
    def __init__(self, text: str):
        self._text = text

    def get_text(self) -> str:
        return self._text