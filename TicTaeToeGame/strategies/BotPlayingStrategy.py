from TicTaeToeGame.models.Board import Board
from TicTaeToeGame.models.CellStatus import CellStatus


class BotPlayingStrategy:
    def move(self, board):
        pass

import random
class EasyBotPlayingStrategy(BotPlayingStrategy):
    def play(self, board: list):
        # Randomly select an empty cell
        empty_cells = []
        for row in board:
            for cell in row:
                if cell.get_cellStatus()==CellStatus.EMPTY:
                    empty_cells.append(cell)
        if empty_cells:
            return random.choice(empty_cells)
        return None

class MediumBotPlayingStrategy(BotPlayingStrategy):
    def play(self, board):
        pass
    
class HardBotPlayingStrategy(BotPlayingStrategy):
    def play(self, board):
        pass
# The HardBotPlayingStrategy can be implemented using the Minimax algorithm or any other advanced strategy.