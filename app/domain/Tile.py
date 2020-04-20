from dataclasses import dataclass
from app.domain.TileType import TileType

@dataclass(frozen=True)
class Tile:
    tile_number: int
    tile_type: TileType

    @staticmethod
    def convert_from_int(number: int):
        """
        1-10: Manzu
        11-20: Pinzu
        21-30: Souzu
        31-37: Zihai
        Note: 10, 20, 30 is Red 5.
        """
        if number < 1 or 37 < number:
            raise ValueError
        tile_type = TileType((number - 1) // 10)
        tile_number = (number % 10)
        return Tile(tile_number=tile_number, tile_type=tile_type)

    def get_string(self):
        return str(self.tile_number) + self.tile_type.get_suffix()
