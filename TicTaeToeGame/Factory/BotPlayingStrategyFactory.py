from TicTaeToeGame.models.BotDifficultyLevel import BotDifficultyLevel
from TicTaeToeGame.strategies.BotPlayingStrategy import EasyBotPlayingStrategy, MediumBotPlayingStrategy, \
    HardBotPlayingStrategy


class BotPlayingStrategyFactory:
    @staticmethod
    def create_bot_playing_strategy(difficulty_level):
        match difficulty_level:
            case BotDifficultyLevel.EASY:
                return EasyBotPlayingStrategy()
            case BotDifficultyLevel.MEDIUM:
                return MediumBotPlayingStrategy()
            case BotDifficultyLevel.HARD:
                return HardBotPlayingStrategy()
            case _:
                raise ValueError("Invalid difficulty level")
        