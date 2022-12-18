from data import Stats


class PlayerStats(Stats):
    def __init__(self) -> None:
        super().__init__()
        self.DEFAULT_CHARACTER_CLASS = None
