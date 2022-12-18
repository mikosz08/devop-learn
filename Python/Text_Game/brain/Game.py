
from characters.Player import Player
from utils.Logger import Logger
log = Logger()

class Game():

    def __init__(self) -> None:
        # Create Character
        self.player_character = Player().create()

        log.message(self.player_character.get_stats())
