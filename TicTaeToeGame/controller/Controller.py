from TicTaeToeGame.models.Game import Game, GameBuilder


class Controller:
    def createGame(self, n, players, strategies) -> Game:
        return GameBuilder().set_dimension(n).set_players(players).set_winningStrategy(strategies).build()
    

    def checkgameStatus(self, game: Game):
        return game.get_gameStatus()
        
    def printBoard(self, game: Game):
        print("Current Board:")
        game.get_board().display()

    def undoMove(self, game: Game):
        game.undo()
        pass

    def makeMove(self, game: Game):
        game.make_move()

    def printWinner(self, game: Game):
        winner = game.winner
        if winner:
            print(f"Winner: {winner.get_name()} ({winner.get_symbol()})")
        else:
            print("No winner yet.")

    def printDraw(self, game: Game):
        print("It's a draw!")