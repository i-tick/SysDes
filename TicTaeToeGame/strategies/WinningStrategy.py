from abc import ABC, abstractmethod

from TicTaeToeGame.models.Board import Board
from TicTaeToeGame.models.CellStatus import CellStatus
from TicTaeToeGame.models.Move import Move


class WinningStrategy(ABC):
    def win(self, board: Board, move: Move):
        pass

class HorizontalWinningStrategy(WinningStrategy):
    def win(self, board: Board, move: Move):
        row = move.get_cell().row
        col = move.get_cell().col
        symbol = move.player.symbol
        for c in range(board.n):
            if board.get_cell(row,c).get_cellStatus()!=CellStatus.FILLED or board.get_cell(row, c).get_player().get_symbol() != symbol:
                return False
        return True

class VerticalWinningStrategy(WinningStrategy):
    def win(self, board: Board, move: Move):
        row = move.get_cell().row
        col = move.get_cell().col
        symbol = move.player.symbol
        for r in range(board.n):
            if board.get_cell(r,col).get_cellStatus()!=CellStatus.FILLED or board.get_cell(r, col).get_player().get_symbol() != symbol:
                return False
        return True

class DiagonalWinningStrategy(WinningStrategy):
    def win(self, board: Board, move: Move):
        row = move.get_cell().row
        col = move.get_cell().col
        symbol = move.player.symbol
        if row == col:
            for i in range(board.n):
                if board.get_cell(i,i).get_cellStatus()!=CellStatus.FILLED or board.get_cell(i, i).get_player().get_symbol() != symbol:
                    return False
            return True
        if row + col == board.n - 1:
            for i in range(board.n):
                if board.get_cell(i, board.n-1-i).get_cellStatus()!=CellStatus.FILLED or board.get_cell(i, board.n-1-i).get_player().get_symbol() != symbol:
                    return False
            return True
        return False