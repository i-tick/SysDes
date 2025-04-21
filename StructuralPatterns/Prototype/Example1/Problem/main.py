from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self) -> str:
        """Display the image."""
        pass

class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self) -> str:
        return f"Displaying {self.filename}"
    
if __name__ == "__main__":  
    image = RealImage("example.jpg") # Unecessary loading
    print(image.display())
    # Output: Loading example.jpg
    #         Displaying example.jpg

    # No caching, no need to load again