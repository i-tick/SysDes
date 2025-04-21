from BehavourialPatterns.SOLID.LSP.BadCode import Readable


if __name__ == "__main__":
    file = Readable()
    file.read()
    file.write()  # This will raise an error