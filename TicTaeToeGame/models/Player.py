import sys
import os

from TicTaeToeGame.models.PlayerType import PlayerType
from TicTaeToeGame.models.Symbol import Symbol

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class Player:
    def __init__(self,name:str, symbol:Symbol,playerType: PlayerType):
        self.name = name
        self.symbol = symbol
        self.playerType = playerType

    def set_name(self, name: str):
        self.name = name
    def set_symbol(self, symbol: Symbol):
        self.symbol = symbol
    def set_playerType(self, playerType: PlayerType):
        self.playerType = playerType
    def get_name(self) -> str:
        return self.name
    def get_symbol(self) -> Symbol:
        return self.symbol
    def get_playerType(self) -> PlayerType:
        return self.playerType


    def makeMove(self, board):
        pass