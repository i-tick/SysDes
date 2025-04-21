from Readonly import Readonly

class Readable(Readonly):
    """
    The Readable interface declares a method for reading and writing data.
    """

    def read(self) -> None:
        """
        Read data from the source.
        """
        print("Reading data from the source...")

    