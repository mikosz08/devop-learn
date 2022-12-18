from enum import Enum

class Stats():
    def __init__(self) -> None:
        self.NAME = DEFAULT_NAME
        self.LEVEL = DEFAULT_LEVEL
        self.HP = DEFAULT_HP
        self.MP = DEFAULT_MP
        self.ATT = DEFAULT_ATT
        self.SPD = DEFAULT_SPD
        self.DEF = DEFAULT_DEF
        self.RACE = DEFAULT_RACE

class Race(Enum):
    HUMAN = 1
    ORC = 2
    NAZIR = 3

class CharacterClass(Enum):
    WARRIOR = 1
    WARLOCK = 2
    SCOUNDREL = 3

DEFAULT_NAME = f"Bob"
DEFAULT_LEVEL = 1
DEFAULT_HP = 100
DEFAULT_MP = 100
DEFAULT_ATT = 10
DEFAULT_DEF = 10
DEFAULT_SPD = 10

DEFAULT_RACE = Race(1)
DEFAULT_CHARACTER_CLASS = CharacterClass(1)
