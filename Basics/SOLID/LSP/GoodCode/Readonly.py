from abc import ABC, abstractmethod
class Readonly(ABC):
    """
    The Readonly interface declares a method for reading data.
    """

    @abstractmethod
    def read(self) -> None:
        pass