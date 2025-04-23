import sys
import os

from TicTaeToeGame.models.Bot import Bot
from TicTaeToeGame.models.BotDifficultyLevel import BotDifficultyLevel
from TicTaeToeGame.models.Human import Human
from TicTaeToeGame.strategies.WinningStrategy import HorizontalWinningStrategy, VerticalWinningStrategy, \
    DiagonalWinningStrategy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TicTaeToeGame.models.GameStatus import GameStatus
from TicTaeToeGame.models.Symbol import Symbol
from TicTaeToeGame.controller.Controller import Controller
from TicTaeToeGame.models.PlayerType import PlayerType
from TicTaeToeGame.models.WinnigEnums import WinningEnums
if __name__ == "__main__":
    # Create a Board
    controller = Controller()
    n = 3
    players = []
    players.append(Human("Player 1", Symbol('X')))
    players.append(Bot("Player 2", Symbol('0'), BotDifficultyLevel.EASY))

    strategies = [HorizontalWinningStrategy(), VerticalWinningStrategy(), DiagonalWinningStrategy()]

    game = controller.createGame(n, players, strategies)



    # if game in progress
    while controller.checkgameStatus(game) == GameStatus.IN_PROGRESS:
        # print board
        controller.printBoard(game)
        # if undo -> call undo
        undo = input("Do you want to undo the last move? (y/n): ")
        if undo.lower() == 'y':
            controller.undoMove(game)
            continue
        # move next player
        controller.makeMove(game)

    
    # check game status
    if controller.checkgameStatus(game) == GameStatus.END:
        # if winner -> print winner
        controller.printWinner(game)
    else:
        # if draw -> print draw
        controller.printDraw(game)