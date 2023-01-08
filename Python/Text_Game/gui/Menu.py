from gui.Text import Text
from gui.game_settings import *


class Menu():
    def __init__(self, surface) -> None:
        self.surface = surface

    def draw_game_title(self):
        title_text = Text(WIN_TITLE, 56, C_WHITE)
        title_text.draw_centered(
            self.surface, adjust_pos(WINDOW_TOP_POS, 0, 35))
