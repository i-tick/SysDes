class file:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    def show_details(self):
        return f"File: {self.name}"
    
    
class folder:
    items = []
    def __init__(self, name):
        self.name = name
        

    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def show_details(self):
        details = f"Folder: {self.name}\n"
        for item in self.items:
            details += f"  - {item.show_details()}\n"
        return details
    
if __name__ == "__main__":
    # Create files
    file1 = file("file1.txt")
    file2 = file("file2.txt")

    # Create folders
    folder1 = folder("folder1")

    # Add files to folders
    folder1.add(file1)
    folder1.add(file2)

    # Display the structure
    print(folder1.show_details())
    # No same implementation of folder and file