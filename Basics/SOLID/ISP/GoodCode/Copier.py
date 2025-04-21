from abc import ABC, abstractmethod
from GoodCode.Document import Document
class Copier(ABC):
    @abstractmethod
    def copy(self, document: Document ):
        pass