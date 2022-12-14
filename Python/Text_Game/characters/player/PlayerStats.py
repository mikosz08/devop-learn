from characters.Stats import Stats
from data.default_statistics import DEFAULT_CHARACTER_CLASS


class PlayerStats(Stats):
    def __init__(self) -> None:
        super().__init__()
        self.CHARACTER_CLASS = DEFAULT_CHARACTER_CLASS

    def __str__(self) -> str:
        return f""" {super().__str__()}CLASS: {self.CHARACTER_CLASS.name}"""
