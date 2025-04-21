class Target:
    """The Target defines the domain-specific interface used by the client code."""
    def request(self) -> str:
        return "Target: The default target's behavior."

def client_code(target: Target) -> None:
    """Client code that works with the target."""
    print(target.request())
    print("Client code is working with the target.")


class Adaptee:
    """The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """
    def specific_request(self) -> str:
        return ".eetpadA eht fo esuaceb ot erehT"
    

class Adapter(Target):
    """The Adapter makes the Adaptee's interface compatible with the Target's
    interface.
    """
    def __init__(self, adaptee: Adaptee) -> None:
        self._adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self._adaptee.specific_request()[::-1]}"
    
if __name__ == "__main__":
    target = Target()
    client_code(target)
    print()

    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client_code(adapter)
