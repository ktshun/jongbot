from enum import Enum

class TileType(Enum):
    MANZU = 0
    PINZU = 1
    SOUZU = 2
    ZIHAI = 3

    def get_suffix(self) -> str:
        if self == TileType.MANZU:
            return 'm'
        elif self == TileType.PINZU:
            return 'p'
        elif self == TileType.SOUZU:
            return 's'
        elif self == TileType.ZIHAI:
            return 'z'

    def get_tile_list(self, is_samma: bool=False, include_red: bool=False) -> list:
        if self == TileType.ZIHAI:
            raw_list = [1,2,3,4,5,6,7] * 4
        elif self == TileType.MANZU and is_samma:
            raw_list = [1,9] * 4
        elif include_red:
            raw_list = [1,2,3,4,6,7,8,9] * 4 + [5] * 3 + [0]
        else:
            raw_list = [1,2,3,4,5,6,7,8,9] * 4
        return map(lambda x: x + self.value * 10, raw_list)
