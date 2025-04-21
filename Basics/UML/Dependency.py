# Document class (provides content to be printed)
class Document:
    def __init__(self, content):
        self.content = content

    def get_content(self):
        return self.content


# Printer class (depends on Document to print)
class Printer:
    def print(self, doc):
        print(f"Printing document: {doc.get_content()}")


# Main function demonstrating Dependency relationship
if __name__ == "__main__":
    doc = Document("Dependency Example Document")
    printer = Printer()

    # Printer depends on Document to print its content
    printer.print(doc)  # Output: Printing document: Dependency Example Document