from typing import override

from TicTaeToeGame.Factory.BotPlayingStrategyFactory import BotPlayingStrategyFactory
from TicTaeToeGame.models.Board import Board
from TicTaeToeGame.models.BotDifficultyLevel import BotDifficultyLevel
from TicTaeToeGame.models.Move import Move
from TicTaeToeGame.models.Player import Player
from TicTaeToeGame.models.PlayerType import PlayerType
from TicTaeToeGame.models.Symbol import Symbol


class Bot(Player):
    def __init__(self, name: str, symbol: Symbol, botDiffucltylevel: BotDifficultyLevel):
        super().__init__(name, symbol, PlayerType.BOT)
        self.botDifficultylevel = botDiffucltylevel
        self.botPlayingStrategy = BotPlayingStrategyFactory.create_bot_playing_strategy(self.botDifficultylevel)

    @override
    def makeMove(self, board: list):
        return Move(self,self.botPlayingStrategy.play(board))
        

    def set_botDifficultylevel(self, botDifficultylevel: BotDifficultyLevel):
        self.botDifficultylevel = botDifficultylevel
    def get_botDifficultylevel(self) -> BotDifficultyLevel:
        return self.botDifficultylevel