from asyncio import current_task
from operator import truediv

from TicTaeToeGame.models.Cell import Cell
from TicTaeToeGame.models.CellStatus import CellStatus
from TicTaeToeGame.models.GameStatus import GameStatus
from TicTaeToeGame.models.Board import Board
from TicTaeToeGame.models.Move import Move
from TicTaeToeGame.models.PlayerType import PlayerType

class GameBuilder:
    def __init__(self):
        self.n  = 0
        self.players = []
        self.winningStrategy = []

    def set_dimension(self, n: int):
        self.n = n
        return self

    def set_players(self, players: int):
        self.players = players
        return self


    def set_winningStrategy(self, winningStrategy: int):
        self.winningStrategy = winningStrategy
        return self

    def build(self):
        return Game(self)

class Game:
    def __init__(self, gameBuilder: GameBuilder ):
        self.board = Board(gameBuilder.n)
        self.players = gameBuilder.players
        self.winningStrategy = gameBuilder.winningStrategy
        self.moves = []
        self.gameStatus = GameStatus.IN_PROGRESS
        self.currentPlayer_index = 0
        # self.winner = None
        
    def play(self):
        pass
    def move(self,move):
        self.moves.append(move)

    def get_gameStatus(self):
        return self.gameStatus
    def set_gameStatus(self, gameStatus):
        self.gameStatus = gameStatus

    def get_board(self):
        return self.board
        

    def make_move(self):
        currentPlayer = self.players[self.currentPlayer_index]
        move = currentPlayer.makeMove(self.board.get_board())
        cell =move.get_cell()
        if cell.get_cellStatus() == CellStatus.EMPTY:
            print(cell.get_row(), cell.get_col())
            cell.set_cellStatus(CellStatus.FILLED)
            cell.set_player(currentPlayer)
            self.moves.append(move)
            self.currentPlayer_index = (self.currentPlayer_index + 1) % len(self.players)

            if self.check_winner(self.board, move):
                print(f"Player {currentPlayer.get_name()} wins!")
                self.set_gameStatus(GameStatus.END)
                self.winner = currentPlayer
            if len(self.moves) == self.board.get_dimensions() ** 2:
                print("It's a draw!")
                self.set_gameStatus(GameStatus.DRAW)
        else:
            print("Invalid move. Try again.")

    def check_winner(self, board, move):
        for winningStrategy in self.winningStrategy:
            if winningStrategy.win(board, move):
                return True
        return False

    def undo(self):
        if self.moves:
            last_move = self.moves.pop()
            cell = self.board.get_cell(last_move.cell.row, last_move.cell.col)
            cell.set_cellStatus(CellStatus.EMPTY)
            cell.set_player(None)
            self.currentPlayer_index = (self.currentPlayer_index - 1) % len(self.players)
        else:
            print("No moves to undo.")