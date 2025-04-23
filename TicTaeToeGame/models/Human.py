from typing import override


from TicTaeToeGame.models.Cell import Cell
from TicTaeToeGame.models.BotDifficultyLevel import BotDifficultyLevel
from TicTaeToeGame.models.Move import Move
from TicTaeToeGame.models.Player import Player
from TicTaeToeGame.models.PlayerType import PlayerType
from TicTaeToeGame.models.Symbol import Symbol


class Human(Player):
    def __init__(self, name: str, symbol: Symbol):
        super().__init__(name, symbol, PlayerType.HUMAN)

    @override
    def makeMove(self, board: list):
        print(f"Current Player: {self.get_name()} ({self.get_symbol()})")
        print("Enter your move (row and column): ")
        row = int(input("Row: "))
        col = int(input("Column: "))

        return Move(self, board[row][col])