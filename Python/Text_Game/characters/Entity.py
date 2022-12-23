from characters.Stats import Stats
from abc import ABC, abstractmethod

class Entity(ABC):

    stats = None

    def __init__(self, stats: Stats) -> None:
        self.stats = stats

    @abstractmethod
    def get_stats(self) -> Stats:
        pass
