import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self):
        pass


