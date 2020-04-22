from flask import Blueprint, jsonify, request
from app.controller.slack.DealResponse import DealResponse
from app.domain.Game import Game
from app.domain.Tile import Tile
from app.domain.TileType import TileType
from app.domain.Wall import Wall
from app.formatter.HandFormatter import format_to_stamp

app = Blueprint('app', __name__)

@app.route('/', methods = ['POST'])
def slash_command():
    ## parse request
    option = request.form['text']
    is_sanma = 'sanma' in option
    include_red = 'aka' in option

    ## Initialize Game
    game = Game(is_sanma=is_sanma, include_red=[include_red, include_red, include_red])
    my_hand = game.my_hand

    response = DealResponse(format_to_stamp(my_hand))
    return jsonify(response)
