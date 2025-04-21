class GamePiece:
    def __init__(self, name: str, color: str, position: tuple = (0, 0)):
        self.name = name
        self.color = color
        self.position = (0, 0)

    def __str__(self):
        return f"GamePiece(name={self.name}, color={self.color}, position={self.position})"

class GameBoard:
    def __init__(self):
        self.pieces = []

    def add_piece(self, piece: GamePiece):
        self.pieces.append(piece)

    def get_pieces(self):
        return self.pieces

    def display(self):
        for piece in self.pieces:
            print(piece)

if __name__ == "__main__":
    board = GameBoard()
    piece1 = GamePiece("Knight", "Black")
    piece2 = GamePiece("Bishop", "White")
    board.add_piece(piece1)
    board.add_piece(piece2)
    print("Original Board:")
    board.display()

    copiedBoard = GameBoard()
    for piece in board.get_pieces():
        copiedBoard.add_piece(GamePiece(piece.name, piece.color, piece.position))
    print("\nCopied Board:")
    copiedBoard.display()
    # Inflexible and difficult to maintain
    # // this is where prototype pattern comes into picture
    # // Prototype pattern allows us to create new objects by copying existing ones
    # // without knowing the details of their classes
    # // This is useful when we want to create a large number of similar objects
    # // or when we want to create objects with different configurations
    # // without having to write a lot of code