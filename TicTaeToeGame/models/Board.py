from TicTaeToeGame.models.Cell import Cell
from TicTaeToeGame.models.CellStatus import CellStatus


class Board:
    def __init__(self, n: int):
        self.n = n
        self.board = []
        for r in range(n):
            row = []
            for c in range(n):
                row.append(Cell(r,c))
            self.board.append(row)

    def get_board(self):
        return self.board
    def get_dimensions(self):
        return self.n
    
    def get_cell(self, row: int, col: int) -> Cell:
        return self.board[row][col]
    def set_cell(self, row: int, col: int, cell: Cell):
        self.board[row][col] = cell
    def display(self):
        for row in self.board:
            for cell in row:
                if cell.get_cellStatus()==CellStatus.EMPTY:
                    print("-", end=" ")
                else:
                    print(cell.display(), end = " ")
            print()
    