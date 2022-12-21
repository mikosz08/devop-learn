from characters.Entity import Entity
from data.PlayerStats import PlayerStats
from data import game_file_paths as paths
from persistance.Persistance import Persistance


class Player(Entity):

    stats = None

    def __init__(self) -> None:
        super().__init__()

        self.stats = PlayerStats()

        Persistance.save(self, paths.ENTITIES_FILE_PATH)
        Persistance.load(paths.ENTITIES_FILE_PATH)

    def get_stats(self) -> PlayerStats:
        return super().get_stats()
