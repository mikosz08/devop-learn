from data.default_statistics import *


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

    def __str__(self) -> str:
        return f"""
===CHARACTER INFO===
NAME: {self.NAME}
LEVEL: {self.LEVEL}
HP: {self.HP}
MP: {self.MP}
ATT: {self.ATT}
SPD: {self.SPD}
DEF: {self.DEF}
RACE: {self.RACE.name}
"""
