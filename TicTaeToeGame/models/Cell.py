from TicTaeToeGame.models.CellStatus import CellStatus
from TicTaeToeGame.models.Player import Player


class Cell:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.cellStatus = CellStatus.EMPTY

    def set_row(self, row: int):
        self.row = row
    def set_col(self, col: int):
        self.col = col
    def set_cellStatus(self, cellStatus: CellStatus):
        self.cellStatus = cellStatus
    def get_row(self) -> int:
        return self.row
    def get_col(self) -> int:
        return self.col
    def get_cellStatus(self) -> CellStatus:
        return self.cellStatus
    def set_player(self, player: Player):
        self.player = player
    def get_player(self) ->  Player:
        return self.player
    def display(self) -> str:
        return self.player.get_symbol().get_achar()