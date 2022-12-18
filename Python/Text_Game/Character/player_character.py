
from Character.character_statistics import *


class PlayerCharacter():
    def __init__(self) -> None:
        self.NAME = DEFAULT_NAME
        self.LEVEL = DEFAULT_LEVEL
        self.CHARACTER_CLASS = DEFAULT_CHARACTER_CLASS
        self.HP = DEFAULT_HP
        self.MP = DEFAULT_MP
        self.ATT = DEFAULT_ATT
        self.SPD = DEFAULT_SPD
        self.DEF = DEFAULT_DEF
        self.RACE = DEFAULT_RACE

    def create(self):
        print("[Creating Character ...]")
        # TODO

        return self

    def show_statistics(self):
        print(self)

    def __str__(self) -> str:
        return (f"""
        NAME:\t{self.NAME}
        LEVEL:\t{self.LEVEL}
        CLASS:\t{self.CHARACTER_CLASS.name}
        HEALTH:\t{self.HP}
        MANA:\t{self.MP}
        ATT:\t{self.ATT}
        SPD:\t{self.SPD}
        DEF:\t{self.DEF}
        RACE:\t{self.RACE.name}
        """)
