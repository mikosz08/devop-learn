import pygame
from gui.Button import Button
from gui.game_settings import *
from gui.types.StateType import StateType


class Menu():
    def __init__(self, surface, buttons_info, draw_pos) -> None:
        self.surface = surface
        self.menu_pos_to_button = self.create_buttons(
            buttons_info, 50, draw_pos)

    def draw_menu_title(self, text):
        title_text = Button(text, 56, C_WHITE, None)
        title_text.draw_centered(
            self.surface, adjust_pos(WINDOW_TOP_POS, 0, 35))

    def check_menu_buttons(self):
        for button in self.menu_pos_to_button:
            pos = pygame.mouse.get_pos()
            collision_detected = button.rect.collidepoint(pos)
            if collision_detected:
                self.clicked_button:Button = button
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

    #Wyniesc do klasy InputField, dodac max len dla textu
    def draw_input_field(self, text, pos, text_size, field_len):
        input_field_button = Button(text, text_size, C_WHITE, StateType.GETTING_USER_INPUT)
        
        text_pos = input_field_button.rect
        text_pos.x, text_pos.y = pos
        
        input_rect = pygame.Rect(
            text_pos.x, text_pos.y, field_len, text_size*2)
        input_rect.center = pos
        
        self.menu_pos_to_button[input_field_button] = input_rect
        
        pygame.draw.rect(self.surface, C_BLACK, input_rect)
        input_field_button.draw_centered(self.surface, pos)

    def update_input_field(self, input):
        self.clear_input_field()
        self.clicked_button.set_text(self.clicked_button.text.get_text() + input)
        self.clicked_button.draw_centered(self.surface, WINDOW_CENTER_POS)
        
    def clear_input_field(self):
        rect = self.menu_pos_to_button[self.clicked_button]
        pygame.draw.rect(self.surface, C_BLACK, rect)


        
