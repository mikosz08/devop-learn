from characters.Entity import Entity
from characters.player.PlayerStats import PlayerStats
from data import game_file_paths as paths
from data.persistance.Persistance import Persistance


class Player(Entity):

    def __init__(self, player_stats: PlayerStats) -> None:
        super().__init__(player_stats)

    def get_stats(self) -> PlayerStats:
        return self.stats
