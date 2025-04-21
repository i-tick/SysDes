import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from abc import abstractmethod

from Basics.OOPS.PaymentMethod import PaymentMethod


class Card (PaymentMethod):
    def __init__(self, card_number, username):
        # private variables
        self.__card_number = None
        self.__username = None
        # # protected variables
        # self._card_number = None
        # self._username = None
        # # public variables
        # self.card_number = card_number
        # self.username = username

    # Getter for username
    def get_username(self):
        return self.__username

    def get_card_number(self):
        return self.__card_number