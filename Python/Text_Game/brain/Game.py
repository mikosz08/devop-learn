from characters.Player import Player
from utils.Logger import Logger


class Game():

    def __init__(self) -> None:
        # Create Character
        self.player_character = Player()

        Logger.log_value(self.player_character)
        Logger.log_value(self.player_character.get_stats())
        
        
