import pygame
from gui.menus.MainMenu import MainMenu
from gui.menus.StartMenu import StartMenu

from gui.StateManager import StateManager
from gui.Text import Text
from gui.types.StateType import StateType
from gui.game_settings import *
from utils.Logger import Logger


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
        # Set game state:
        self.state_manager = StateManager(
            self.main_surface, initial_state=StateType.IN_MAIN_MENU)
        # Draw:
        self.draw()

    def draw(self):
        self.fill_black()
        game_state = self.state_manager.get_game_state()
        match game_state:
            case StateType.IN_MAIN_MENU:
                self.main_menu = MainMenu(self.main_surface)
                self.main_menu.draw_main_menu()
                Logger.log_message("Entered Main Menu")

            case StateType.IN_START_MENU:
                self.start_menu = StartMenu(self.main_surface)
                self.start_menu.draw_start_menu()
                Logger.log_message("Entered Start Menu")

            case StateType.IN_CREDITS_MENU:
                self.main_surface.fill(C_NAVY)
                Logger.log_message("Entered Credits Menu")

            case StateType.IN_QUIT_MENU:
                Logger.log_message("Entered Quit Menu")

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def check_state(self):
        mouse_pressed = pygame.mouse.get_pressed()[0] == 1
        if mouse_pressed:
            current_state = self.state_manager.get_game_state()
            match current_state:
                case StateType.IN_MAIN_MENU:
                    new_state = self.main_menu.check_main_menu_buttons()
                    if new_state != None:
                        self.state_manager.set_game_state(new_state)
                        self.draw()
                case StateType.IN_START_MENU:
                    pass
                case StateType.IN_CREDITS_MENU:
                    pass
                case StateType.IN_QUIT_MENU:
                    self.running = False
                case StateType.IN_GAME:
                    pass

    def fill_black(self):
        self.main_surface.fill(C_BLACK)

    def draw_utils(self):
        self.draw_window_positions()
        self.draw_fps()

    def update(self):
        self.main_display.update()
        self.clock.tick(self.fps)

    def main_loop(self):
        while (self.running):
            self.check_events()
            self.check_state()
            self.draw_utils()
            self.update()
        pygame.quit()

# Utils
# Wynieśc do klasy UtilityDraw
    def draw_fps(self):
        # Create fps_text Text object:
        fps = int(self.clock.get_fps())
        fps = "{:.1f}".format(fps)
        fps_text = Text(text=fps, size=15, color=C_WHITE, tag="FPS")
        pos = WINDOW_BOTTOM_RIGHT_POS

        # Create rect to cover previous fps_text:
        clear_rect_size = (fps_text.surface.get_width(),
                           fps_text.surface.get_height())
        clear_rect_pos = fps_text.rect
        clear_rect_pos.x, clear_rect_pos.y = pos
        rect = pygame.Rect(clear_rect_pos.x, clear_rect_pos.y,
                           clear_rect_size[0], clear_rect_size[1])
        pygame.draw.rect(self.main_surface, C_BLACK, rect)

        # Draw fps_text:
        fps_text.draw(self.main_surface, pos)

    # Wynieśc do klasy UtilityDraw
    def draw_window_positions(self):
        pos_char = ord('A')
        for pos in WIN_POSITIONS:
            # Draw character representing the position:
            text = Text(f"{chr(pos_char)}", 15, C_GREEN, "")
            text.draw(self.main_surface, pos)
            pos_char += 1
