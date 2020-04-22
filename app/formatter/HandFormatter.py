from PIL import Image
from typing import List
from app.domain.Tile import Tile

def format_to_image(hand: List[Tile]):
    formatted_image = Image.new('RGB', (32 * 14, 45))
    x = 0
    for tile in hand:
        image = Image.open('app/image/' + tile.get_string() + '.png')
        formatted_image.paste(image, (x, 0))
        x += 32
    return formatted_image

def format_to_stamp(hand: List[Tile]):
    formatted = '';
    for tile in hand:
        formatted += ' :{}: '.format(tile.get_string())
    return formatted
