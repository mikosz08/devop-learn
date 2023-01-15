from gui.Text import Text
from gui.game_settings import *


class Menu():
    def __init__(self, surface) -> None:
        self.surface = surface

    def draw_game_title(self):
        title_text = Text(WIN_TITLE, 56, C_WHITE)
        title_text.draw_centered(
            self.surface, adjust_pos(WINDOW_TOP_POS, 0, 35))
        
    def create_buttons(self, txt_and_size_dict, offset, pos):
        buttons_and_positions_dict = dict()
        for button_text in txt_and_size_dict:
            # Create Button:
            text_tag = button_text.split()[0]
            text_size = txt_and_size_dict[button_text]
            button = Text(button_text, text_size, C_WHITE, text_tag)
            # Save button position:
            buttons_and_positions_dict[button] = pos
            # Update position:
            pos = (pos[0], pos[1] + offset)
        return buttons_and_positions_dict