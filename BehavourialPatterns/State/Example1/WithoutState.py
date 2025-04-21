from enum import Enum

class TransportationMode(Enum):
    WALKING = 1
    CYCLING = 2
    CAR = 3
    TRAIN = 4


class DirectionService:
    def __init__(self, mode: TransportationMode):
        self.mode = mode

    def set_mode(self, mode: TransportationMode):
        self.mode = mode

    def get_eta(self) -> int:
        match self.mode:
            case TransportationMode.WALKING:
                print("Calc ETA for walking 10")
                return 10
            case TransportationMode.CYCLING:
                print("Calc ETA for cycling 5")
                return 5
            case TransportationMode.CAR:
                print("Calc ETA for car 2")
                return 2
            case TransportationMode.TRAIN:
                print("Calc ETA for train 3")       
                return 3
            case _:
                raise ValueError("Unknown Mode")

    def get_direction(self) -> str:
        match self.mode:
            case TransportationMode.WALKING:
                return "Directions for walking: Head north for 500 meters."
            case TransportationMode.CYCLING:
                return "Directions for cycling: Take the bike lane on Elm Street."
            case TransportationMode.CAR:
                return "Directions for driving: Use highway 50 towards downtown."
            case TransportationMode.TRAIN:
                return "Directions for train: Board the Red Line at Central Station."
            case _:
                return "No directions available for the selected mode."
       
if __name__ == "__main__":
    service = DirectionService(TransportationMode.WALKING)
    print(service.get_eta())
    print(service.get_direction())
    service.set_mode(TransportationMode.CYCLING)
    print(service.get_eta())
    print(service.get_direction())