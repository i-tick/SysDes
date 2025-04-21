import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from TextEditor import TextEditor
from Helper import Helper

if __name__ == "__main__":

    editor = TextEditor()
    helper = Helper()

    # Type some text
    editor.write("Hello")
    helper.save_state(editor)
    print(editor.text)  # Output: Hello

    # Type more text
    editor.write(", World!")
    helper.save_state(editor)
    print(editor.text)  # Output: Hello, World!

    # Undo the last change
    helper.restore_state(editor)
    print(editor.text)  # Output: Hello

    helper.restore_state(editor)
    print(editor.text)  # Output: Empty
    