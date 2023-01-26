from gui.menus.Menu import Menu
from gui.game_settings import *


class NewGameMenu(Menu):
    def __init__(self, surface, buttons_info, pos) -> None:
        super().__init__(surface, buttons_info, pos)

    def draw_menu(self):
        self.draw_menu_title("Create Character")
        self.draw_buttons()
        self.draw_input_field(
            "Character Name", WINDOW_CENTER_POS, text_size=20, field_len=175)

    def draw_buttons(self):
        for button in self.menu_pos_to_button:
            size = self.menu_pos_to_button[button]
            button.draw_centered(self.surface, size)
