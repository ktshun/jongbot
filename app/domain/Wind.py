from enum import Enum

class Wind(Enum):
    EAST = 0
    SOUTH = 1
    WEST = 2
    NORTH = 3

    def get_string(self):
        if self == Wind.EAST:
            return "東"
        elif self == Wind.SOUTH:
            return "南"
        elif self == Wind.WEST:
            return "西"
        elif self == Wind.NORTH:
            return "北"
    
