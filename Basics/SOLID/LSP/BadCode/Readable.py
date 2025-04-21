from BehavourialPatterns.SOLID.LSP.BadCode import File


class Readable(File):

    def write(self):
        raise NotImplementedError("Cannot write to a readable file")

    