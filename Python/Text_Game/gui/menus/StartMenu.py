from gui.menus.Menu import Menu
from gui.types.ButtonType import ButtonType
from gui.game_settings import *


class StartMenu(Menu):
    def __init__(self, surface) -> None:
        super().__init__(surface)

    def draw_menu(self):
        self.draw_start_menu_buttons()

    def draw_start_menu_buttons(self):
        text_size_dict = {ButtonType.CONTINUE_BUTTON.value: 46,
                          ButtonType.NEW_GAME_BUTTON.value: 40,
                          ButtonType.BACK_BUTTON.value: 36}
        self.main_menu_buttons = self.create_buttons(
            text_size_dict, 50, WINDOW_CENTER_POS)
        for button in self.main_menu_buttons:
            button.draw_centered(self.surface, self.main_menu_buttons[button])
