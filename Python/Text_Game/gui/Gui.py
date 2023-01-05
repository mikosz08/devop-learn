import pygame
from gui.Text import Text
from utils.Logger import Logger
from gui.StateType import StateType
from gui.game_settings import *


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
        self.change_state(StateType.IN_MAIN_MENU)
        Logger.log_message("Game loop starts")

    def tick(self):
        self.clock.tick(self.fps)

    # Wynieśc do klasy Menu
    def draw_menu(self):
        self.menu_buttons = list()
        text_size_dict = {'Start': 46, 'Quit': 36, 'Credits': 26}
        offset = 50
        pos = WINDOW_CENTER_POS
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

    # Wynieśc do klasy GameTitle
    def draw_game_title(self):
        title_text = Text(WIN_TITLE, 56, C_WHITE)
        title_text.draw_centered(
            self.main_surface, adjust_pos(WINDOW_TOP_POS, 0, 35))

    # Wynieśc do klasy UtilityDraw
    def draw_fps(self):
        fps = int(self.clock.get_fps())
        fps = "{:.1f}".format(fps)
        fps_text = Text(fps, 15, C_WHITE, "FPS")

        clear_rect_size = (-6, 14)
        clear_rect_pos = fps_text.rect
        clear_rect_pos.x, clear_rect_pos.y = adjust_pos(
            WINDOW_BOTTOM_RIGHT_POS, width_height_tuple=clear_rect_size)
        rect = pygame.Rect((clear_rect_pos.x, clear_rect_pos.y, 33, 15))
        pygame.draw.rect(self.main_surface, C_BLACK, rect)

        fps_text.draw_centered(self.main_surface, adjust_pos(
            WINDOW_BOTTOM_RIGHT_POS, 10, 20))

    # Wynieśc do klasy UtilityDraw
    def draw_window_positions(self):
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
            mouse_pressed = pygame.mouse.get_pressed()[0] == 1
            collision_detected = rect.collidepoint(pos)

            if collision_detected and mouse_pressed:

                if self.game_state == StateType.IN_MAIN_MENU:

                    if button.tag == "Start":
                        self.change_state(StateType.IN_START_MENU)
                    elif button.tag == "Quit":
                        self.change_state(StateType.QUIT)
                    else:
                        print('h')

                elif self.game_state == StateType.IN_START_MENU:
                    pass

                elif self.game_state == StateType.IN_CHARACTER_CREATION:
                    pass

                elif self.game_state == StateType.IN_GAME:
                    pass

    # Wynieść do klasy State
    def change_state(self, state):
        self.game_state = state
        self.state_entered = False

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw_utils(self):
        self.draw_window_positions()
        self.draw_fps()

    def check_gui_state(self):
        if self.state_entered: 
            return
        

        
        if self.game_state == StateType.IN_MAIN_MENU:
            self.draw_game_title() # z klasy GameTitle
            self.draw_menu() # z klasy Menu
            self.state_entered = True
            Logger.log_message("Entered Main Menu")
        elif self.game_state == StateType.IN_START_MENU:
            self.main_surface.fill(C_BLACK)
            self.state_entered = True
            Logger.log_message("Entered Start Menu")
        elif self.game_state == StateType.QUIT:
            self.running = False

    def update(self):
        self.main_display.update()
        self.tick()

    def main_loop(self):
        while (self.running):
            self.check_events()
            self.check_gui_state()
            self.check_buttons()
            self.draw_utils()
            self.update()
        pygame.quit()
