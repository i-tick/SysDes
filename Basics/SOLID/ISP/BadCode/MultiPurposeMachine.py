from Machine import Machine


class MultiPurposeMachine(Machine):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

    def copy(self, document):
        print(f"Copying: {document}")