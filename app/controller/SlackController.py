from flask import Blueprint, jsonify
from app.controller.slack.DealResponse import DealResponse
from app.domain.Game import Game
from app.domain.Tile import Tile
from app.domain.TileType import TileType
from app.domain.Wall import Wall
from app.formatter.HandFormatter import format_to_stamp

app = Blueprint('app', __name__)

@app.route('/', methods = ['POST', 'GET' ])
def slash_command():
    game = Game()
    my_hand = game.my_hand

    response = DealResponse(format_to_stamp(my_hand))
    return jsonify(response)
