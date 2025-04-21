from Readable import Readable
from WriteOnly import WriteOnly

class Writeable(Readable, WriteOnly):
    """
    The Writeable interface extends the Readonly interface and declares a method for writing data.
    """

    def write(self) -> None:
        """
        Write data to the source.
        """
        print("Writing data to the source...")