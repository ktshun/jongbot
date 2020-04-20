
from app.domain.TileType import TileType
from random import shuffle
from app.domain.Tile import Tile

class Wall:
    def __init__(self, is_sanma: bool=False, include_manzu_red: bool=False, include_pinzu_red: bool=False, include_souzu_red: bool=False):
        tile_list_int = []
        tile_list_int.extend(TileType.MANZU.get_tile_list(is_sanma, include_manzu_red))
        tile_list_int.extend(TileType.PINZU.get_tile_list(False, include_pinzu_red))
        tile_list_int.extend(TileType.SOUZU.get_tile_list(False, include_souzu_red))
        tile_list_int.extend(TileType.ZIHAI.get_tile_list(False, False))
        shuffle(tile_list_int)

        self.tile_list = list(map(lambda x: Tile.convert_from_int(x), tile_list_int))
        self.dora_indicator = self.tile_list[-10]

    def deal(self, is_sanma: bool=False) -> list:
        if is_sanma:
            hands = [[] for i in range(3)]
        else:
            hands = [[] for i in range(4)]

        for i in range(14):
            for j in range(len(hands)):
                hands[j].append(self.tile_list.pop(0))
        sorted_hands = []
        for i in range(len(hands)):
            sorted_hands.append(sorted(hands[i], key=lambda tile: (tile.tile_type.value, tile.tile_number)))

        return sorted_hands

    def draw(self) -> Tile:
        self.tile_list.pop(0)
