from enum import Enum

class Round(Enum):
    EAST = 0
    SOUTH = 1

    def get_string(self):
        if self == Round.EAST:
            return "東場"
        elif self == Round.SOUTH:
            return "南場"
