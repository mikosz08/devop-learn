import pygame
from gui.Button import Button
from gui.game_settings import *


class Menu():
    def __init__(self, surface, buttons_info) -> None:
        self.surface = surface
        self.menu_buttons = self.create_buttons(
            buttons_info, 50, WINDOW_CENTER_POS)

    def draw_game_title(self):
        title_text = Button(WIN_TITLE, 56, C_WHITE, None)
        title_text.draw_centered(
            self.surface, adjust_pos(WINDOW_TOP_POS, 0, 35))

    def check_menu_buttons(self):
        for button in self.menu_buttons:
            pos = pygame.mouse.get_pos()
            collision_detected = button.rect.collidepoint(pos)
            if collision_detected:
                return button.button_type
        return None

    def create_buttons(self, buttons_info, offset, pos):
        pos_to_button = dict()
        for btn_info in buttons_info:
            # Create Button:
            button_text, button_type, text_size = btn_info
            btn_info = Button(button_text, text_size, C_WHITE, button_type)
            # Save button position:
            pos_to_button[btn_info] = pos
            # Update position:
            pos = (pos[0], pos[1] + offset)
        return pos_to_button
