from GoodCode import Printer, Scanner, Copier


class MultiMachine(Printer, Scanner, Copier):
    def print(self, document):
        print(f"Printing document: {document}")

    def scan(self, document):
        print(f"Scanning document: {document}")

    def copy(self, document):
        print(f"Copying document: {document}")