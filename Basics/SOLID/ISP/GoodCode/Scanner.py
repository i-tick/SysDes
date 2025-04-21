from abc import ABC, abstractmethod
from GoodCode.Document import Document
class Scanner(ABC):
    @abstractmethod
    def scan(self, document: Document ):
        pass