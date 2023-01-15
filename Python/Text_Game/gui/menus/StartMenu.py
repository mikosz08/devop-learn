from gui.menus.Menu import Menu
from gui.types.ButtonType import ButtonType
from gui.game_settings import *


class StartMenu(Menu):
    def __init__(self, surface, buttons_info) -> None:
        super().__init__(surface, buttons_info)

    def draw_menu(self):
        self.draw_start_menu_buttons()

    def draw_start_menu_buttons(self):
        for button in self.menu_buttons:
            button.draw_centered(self.surface, self.menu_buttons[button])
