from app.domain.Round import Round
from app.domain.Wall import Wall
from app.domain.Wind import Wind
from random import randrange
from typing import List

class Game:
    def __init__(
        self,
        is_sanma: bool=False,
        include_red: List[bool]=[False, False, False],
        round: Round=Round.EAST,
        round_number: int=1
    ):
        self.member = 3 if is_sanma else 4
        self.round = round
        self.round_number = randrange(self.member)

        self.wall = Wall(is_sanma, include_red[0], include_red[1], include_red[2])
        self.hands = self.wall.deal()

        self.my_wind = Wind(randrange(self.member))
        self.my_hand = self.hands[self.my_wind.value]
