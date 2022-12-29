from enum import Enum
import pygame
from gui.game_settings import *
from gui.Text import Text
from utils.Logger import Logger
from gui.game_states import *


class Gui():

    def __init__(self) -> None:
        pygame.init()
        # Window size:
        self.resolution = (WIN_WIDTH, WIN_HEIGHT)
        # Window title:
        self.title = WIN_TITLE
        # Frames per second:
        self.fps = FPS
        # Game clock:
        self.clock = pygame.time.Clock()
        # Display:
        self.main_display = pygame.display
        self.main_display.set_mode(self.resolution)
        self.main_display.set_caption(self.title)
        # Surface:
        self.main_surface = self.main_display.get_surface()
        # Is game running:
        self.running = True
        self.change_state(IN_MAIN_MENU)
        Logger.log_message("Game loop starts")

    def tick(self):
        self.clock.tick(self.fps)

    def draw_menu(self):
        self.menu_buttons = list()
        text_size_dict = {'Start': 46, 'Quit': 36, 'Credits': 26}
        offset = 50
        pos = WIN_MIDDLE_POS
        for button_text in text_size_dict:
            # Create Button:
            text_tag = button_text.split()[0]
            text_size = text_size_dict[button_text]
            button_text = Text(button_text, text_size, C_WHITE, text_tag)
            button_text.draw_centered(self.main_surface, pos)
            # Save Button:
            self.menu_buttons.append(button_text)
            # Update position:
            pos = (pos[0], pos[1] + offset)

    def draw_game_title(self):
        fps_text = Text(WIN_TITLE, 56, C_WHITE)
        fps_text.draw_centered(self.main_surface, WIN_BOTTOM_RIGHT_POS)

    def draw_fps(self):
        fps = int(self.clock.get_fps())
        fps = "{:.1f}".format(fps)
        # print("tutaj")
        fps_text = Text(fps, 15, C_WHITE, "FPS")
        
        clear_rect_size = (-6, 14)
        clear_rect_pos = fps_text.rect
        clear_rect_pos.x, clear_rect_pos.y = adjust_pos(
            WIN_BOTTOM_RIGHT_POS, width_height_tuple=clear_rect_size)
        rect = pygame.Rect((clear_rect_pos.x,clear_rect_pos.y,33,15))
        pygame.draw.rect(self.main_surface, C_BLACK, rect)

        fps_text.draw_centered(self.main_surface, adjust_pos(WIN_BOTTOM_RIGHT_POS, 10, 20))

    def draw_positions(self):
        pos_char = ord('A')
        for pos in WIN_POSITIONS:
            # Draw character representing the position:
            text = Text(f"{chr(pos_char)}", 15, C_GREEN, "")
            text.draw(self.main_surface, pos)

            pos_char += 1

    def check_buttons(self):
        pos = pygame.mouse.get_pos()
        for button in self.menu_buttons:
            rect = button.rect
            if rect.collidepoint(pos):
                if button.tag == "Start" and pygame.mouse.get_pressed()[0] == 1:
                    self.change_state(IN_START_MENU)
                elif button.tag == "Quit" and pygame.mouse.get_pressed()[0] == 1:
                    self.change_state(QUIT)
                else:
                    pass

    def draw_utils(self):
        self.draw_positions()
        self.draw_fps()

    def update(self):
        self.check_buttons()
        self.main_display.update()
        self.tick()

    def change_state(self, state):
        self.game_state = state
        self.state_entered = False

    def main_loop(self):

        self.state_entered = False

        while (self.running):

            # Check events:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            if self.game_state == IN_MAIN_MENU and self.state_entered == False:
                Logger.log_message("Drew menu buttons")
                # TODO: Wynieść do klasy Menu
                self.draw_menu()
                self.state_entered = True
            elif self.game_state == IN_START_MENU:
                self.main_surface.fill(C_BLACK)
            elif self.game_state == QUIT:
                self.running = False

            self.draw_utils()
            self.update()

        pygame.quit()


# class de(Enum):
#     START = "Start"
#     QUIT = "Quit"
