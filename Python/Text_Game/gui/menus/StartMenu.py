from gui.menus.Menu import Menu
from gui.game_settings import *


class StartMenu(Menu):
    def __init__(self, surface, buttons_info, pos) -> None:
        super().__init__(surface, buttons_info, pos)

    def draw_menu(self):
        self.draw_buttons()

    def draw_buttons(self):
        for button in self.menu_pos_to_button:
            cords = self.menu_pos_to_button[button]
            button.draw_centered(self.surface, cords)
