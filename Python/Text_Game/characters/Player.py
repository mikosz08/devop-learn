from characters.Entity import Entity
from data.Stats import DEFAULT_CHARACTER_CLASS

class Player(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.CHARACTER_CLASS = DEFAULT_CHARACTER_CLASS

    
    