from gui.menus.Menu import Menu
from gui.game_settings import *


class CreditsMenu(Menu):

    def __init__(self, surface, buttons_info) -> None:
        super().__init__(surface, buttons_info)

    def draw_menu(self):
        self.draw_buttons()

    def draw_buttons(self):
        for button in self.menu_buttons:
            button.draw_centered(self.surface, self.menu_buttons[button])
