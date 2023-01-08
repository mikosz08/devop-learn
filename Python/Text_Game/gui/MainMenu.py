from gui.Menu import Menu
from gui.Text import Text
from gui.game_settings import *
from gui.types.ButtonType import ButtonType


class MainMenu(Menu):
    
    def __init__(self, surface) -> None:
        super().__init__(surface)
    
    def draw(self):
        self.draw_game_title()
        self.draw_menu_buttons()
        return self
    
    def draw_menu_buttons(self):
        self.menu_buttons = list()
        text_size_dict = {ButtonType.START_BUTTON.value: 46,
                          ButtonType.QUIT_BUTTON.value: 36,
                          ButtonType.CREDITS_BUTTON.value: 26}
        offset = 50
        pos = WINDOW_CENTER_POS
        for button_text in text_size_dict:
            # Create Button:
            text_tag = button_text.split()[0]
            text_size = text_size_dict[button_text]
            button_text = Text(button_text, text_size, C_WHITE, text_tag)
            button_text.draw_centered(self.surface, pos)
            # Save Button:
            self.menu_buttons.append(button_text)
            # Update position:
            pos = (pos[0], pos[1] + offset)
        
    
    def draw_game_title(self):
        title_text = Text(WIN_TITLE, 56, C_WHITE)
        title_text.draw_centered(
            self.surface, adjust_pos(WINDOW_TOP_POS, 0, 35))
        
    def get_menu_buttons(self):
        return self.menu_buttons