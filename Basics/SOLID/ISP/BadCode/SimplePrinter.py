from Machine import Machine


class SimplePrinter(Machine):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        raise NotImplementedError("This machine cannot scan.")

    def copy(self, document):
        raise NotImplementedError("This machine cannot copy.")