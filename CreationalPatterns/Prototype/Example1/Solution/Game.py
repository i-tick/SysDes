from abc import ABC, abstractmethod
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        """Create a clone of the object."""
        pass

class GamePiece(Prototype):
    def __init__(self, name: str, color: str, position: tuple = (0, 0)):
        self.name = name
        self.color = color
        self.position = position

    def __str__(self):
        return f"{self.color} {self.name} at {self.position}"

    def clone(self):
        return GamePiece(self.name, self.color, self.position)
    
class GameBoard(Prototype):
    def __init__(self):
        self.pieces = []

    def add_piece(self, piece: GamePiece):
        self.pieces.append(piece)

    def get_pieces(self):
        return self.pieces

    def display(self):
        for piece in self.pieces:
            print(piece)
    def clone(self):
        new_board = GameBoard()
        for piece in self.get_pieces():
            # clone the piece and add it to the new board
            # does deep copy instead of shallow copy
            # this is the main difference between prototype and factory
            new_board.add_piece(piece.clone())
        return new_board
    
if __name__ == "__main__":
    board = GameBoard()
    piece1 = GamePiece("Knight", "Black")
    piece2 = GamePiece("Bishop", "White")
    board.add_piece(piece1)
    board.add_piece(piece2)
    print("Original Board:")
    board.display()

    copiedBoard = board.clone()
    print("\nCopied Board:")
    copiedBoard.display()

    # The copied board is a deep copy of the original board
    # 1. Prototype pattern allows us to create new objects by copying existing ones
    # without knowing the details of their classes
    # 2. This is useful when we want to create a large number of similar objects
    # or when we want to create objects with different configurations
    # without having to write a lot of code

    # Ex:  Base SQL Queries
    # Ex:  HTTP Requests
    # Ex:  Game Pieces(Initialization)
    # Ex:  Data Structures
    # Ex:  Configuration Objects
    # Ex:  Network Connections