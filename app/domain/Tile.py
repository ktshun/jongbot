from dataclasses import dataclass
from app.domain.TileType import TileType

@dataclass(frozen=True)
class Tile:
    tile_number: int
    tile_type: TileType

    @staticmethod
    def convert_from_int(number: int):
        """
        0-9: Manzu
        10-19: Pinzu
        20-29: Souzu
        31-37: Zihai
        Note: 0, 10, 20 is Red 5.
        """
        if number < 0 or 37 < number:
            raise ValueError
        tile_type = TileType(number // 10)
        tile_number = (number % 10)
        return Tile(tile_number=tile_number, tile_type=tile_type)

    def get_string(self):
        return str(self.tile_number) + self.tile_type.get_suffix()
