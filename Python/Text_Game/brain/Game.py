from characters.player.Player import Player
from characters.player.PlayerStats import PlayerStats
from utils.Logger import Logger


class Game():

    def __init__(self) -> None:
        # Create Character
        self.player_character = Player(player_stats=PlayerStats())

        Logger.log_value(self.player_character)
        Logger.log_value(self.player_character.get_stats())
        
        
