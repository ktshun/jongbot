from PIL import Image

def format_to_image(hand: list):
    formatted_image = Image.new('RGB', (32 * 14, 45))
    x = 0
    for tile in hand:
        image = Image.open('app/image/' + tile.get_string() + '.png')
        formatted_image.paste(image, (x, 0))
        x += 32
    return formatted_image
