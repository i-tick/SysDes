from abc import ABC, abstractmethod
class WriteOnly(ABC):
    """
    The WriteOnly interface declares a method for writing data.
    """

    @abstractmethod
    def write(self) -> None:
        pass