from TicTaeToeGame.models.Cell import Cell
from TicTaeToeGame.models.Player import Player


class Move:
    def __init__(self, player: Player, cell: Cell):
        self.player = player
        self.cell = cell
    
    def set_player(self, player: Player):
        self.player = player
    def set_cell(self, cell: Cell):
        self.cell = cell
    def get_player(self) -> Player:
        return self.player
    def get_cell(self) -> Cell:
        return self.cell