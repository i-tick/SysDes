class Helper:
    def __init__(self):
        self.history = []
        self.current_state = None

    def save_state(self, editor):
        self.history.append(editor.save())  

    def restore_state(self,editor):
        if self.history:
            print("Restoring to previous state")
            self.history.pop()
            if self.history:
                editor.restore(self.history[-1])
            else:
                editor.restore(None)
        return None