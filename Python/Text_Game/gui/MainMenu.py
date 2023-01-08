import pygame
from gui.Menu import Menu
from gui.Text import Text
from gui.game_settings import *
from gui.types.ButtonType import ButtonType
from gui.types.StateType import StateType


class MainMenu(Menu):

    def __init__(self, surface) -> None:
        super().__init__(surface)

    def draw_main_menu(self):
        self.draw_game_title()
        self.draw_main_menu_buttons()

    def draw_main_menu_buttons(self):
        text_size_dict = {ButtonType.START_BUTTON.value: 46,
                          ButtonType.QUIT_BUTTON.value: 36,
                          ButtonType.CREDITS_BUTTON.value: 26}
        self.main_menu_buttons = self.create_buttons(
            text_size_dict, 50, WINDOW_CENTER_POS)
        for button in self.main_menu_buttons:
            button.draw_centered(self.surface, self.main_menu_buttons[button])

    def check_main_menu_buttons(self):
        for button in self.main_menu_buttons:
            pos = pygame.mouse.get_pos()
            collision_detected = button.rect.collidepoint(pos)
            if collision_detected:
                match button.tag:
                    case ButtonType.START_BUTTON.value:
                        return StateType.IN_START_MENU

                    case ButtonType.CREDITS_BUTTON.value:
                        return StateType.IN_CREDITS_MENU

                    case ButtonType.QUIT_BUTTON.value:
                        return StateType.IN_QUIT_MENU
        return None
