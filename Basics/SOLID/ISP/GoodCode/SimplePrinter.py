from Document import Document
from Printer import Printer


class SimplePrinter(Printer):
    def print(self, document: Document) -> None:
        print(f"Printing document: {document}")
    