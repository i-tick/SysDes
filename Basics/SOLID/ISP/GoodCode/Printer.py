from abc import ABC, abstractmethod
from GoodCode.Document import Document
class Printer(ABC):
    @abstractmethod
    def print(self, document: Document ):
        pass