from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self) -> str:
        """Display the image."""
        pass

class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self) -> str:
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        return self.real_image.display()
    
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_image_from_disk()

    def load_image_from_disk(self):
        print(f"Loading {self.filename}")

    def display(self) -> str:
        return f"Displaying {self.filename}"
    
if __name__ == "__main__":  
    image = ProxyImage("example.jpg") # Unecessary loading
    print(image.display())
    # Output: Loading example.jpg
    #         Displaying example.jpg

    # No caching, no need to load again

    image2 = ProxyImage("example.jpg") # Unecessary loading
    print(image2.display())
    # Output: Loading example2.jpg
    #         Displaying example2.jpg