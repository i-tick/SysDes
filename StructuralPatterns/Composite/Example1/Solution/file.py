from abc import ABC, abstractmethod

class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        """Show details of the component."""
        pass

class file(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    def show_details(self):
        return f"File: {self.name}"
    
    
class folder(FileSystemComponent):
    
    def __init__(self, name):
        self.name = name
        self.items = []  # Initialize items as an empty list
        
    # add filesystem components to the folder
    def add(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

    def show_details(self):
        details = f"Folder: {self.name}\n"
        print(f"Items in {self.items}:")
        for item in self.items:
            details += f"{item.show_details()}\n"
        return details
    
if __name__ == "__main__":
    # Create files
    file1 = file("file1.txt")
    file2 = file("file2.txt")
    file3 = file("file3.txt")

    # Create folders
    folder1 = folder("folder1")
    folder2 = folder("folder2")

    # Add files to folders
    folder1.add(file1)
    folder1.add(file2)
    folder2.add(file3)

    root_folder = folder("root")
    root_folder.add(folder1)
    root_folder.add(folder2)

    # Display the structure
    
    print(root_folder.show_details())
    # same implementation of folder and file
    # uniform interface and scalability