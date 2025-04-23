from strategies.WinningStrategy import HorizontalWinningStrategy, VerticalWinningStrategy, DiagonalWinningStrategy
from models.WinningEnums import WinningEnums
class WinningStrategyFactory:
    """
    Factory class to create winning strategies for Tic Tac Toe.
    """

    @staticmethod
    def create_winning_strategy(strategy_type):
        """
        Create a winning strategy based on the provided type.

        :param strategy_type: Type of winning strategy to create.
        :return: An instance of the specified winning strategy.
        """
        if strategy_type == WinningEnums.Horizontal:
            return HorizontalWinningStrategy()
        elif strategy_type == WinningEnums.Vertical:
            return VerticalWinningStrategy()
        elif strategy_type == WinningEnums.Diagonal:
            return DiagonalWinningStrategy()
        else:
            raise ValueError(f"Unknown strategy type: {strategy_type}")