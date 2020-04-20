from flask import Blueprint
from app.domain.Game import Game
from app.domain.Tile import Tile
from app.domain.TileType import TileType
from app.domain.Wall import Wall

app = Blueprint('app', __name__)

@app.route('/deal')
def deal():
    game = Game()
    my_hand = game.my_hand
    return ''.join(map(lambda x: x.get_string(), my_hand))
