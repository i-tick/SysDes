import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Basics.OOPS.Card import Card


class DebitCard(Card):
    def __init__(self, card_number, username):
        super().__init__(card_number, username)

    def pay(self):
        print(f"Paid using Debit Card {self.get_card_number()} for user {self.get_username()}")