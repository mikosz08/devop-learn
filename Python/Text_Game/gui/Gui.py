import pygame
from gui.Button import Button
from gui.menus.CreditsMenu import CreditsMenu
from gui.menus.MainMenu import MainMenu
from gui.menus.StartMenu import StartMenu
from gui.StateManager import StateManager
from gui.Text import Text
from gui.types.ButtonType import *
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
        self.state_manager = StateManager(initial_state=StateType.IN_MAIN_MENU)
        # Draw:
        self.draw()

    def draw(self):
        self.fill_black()
        game_state = self.state_manager.get_game_state()
        match game_state:
            case StateType.IN_MAIN_MENU:
                self.current_menu = MainMenu(
                    self.main_surface, MAIN_MENU_BUTTONS)
                self.current_menu.draw_menu()
                Logger.log_message("Entered Main Menu")

            case StateType.IN_START_MENU:
                self.current_menu = StartMenu(
                    self.main_surface, START_MENU_BUTTONS)
                self.current_menu.draw_menu()
                Logger.log_message("Entered Start Menu")

            case StateType.IN_CREDITS_MENU:
                self.current_menu = CreditsMenu(
                    self.main_surface, CREDITS_MENU_BUTTONS)
                self.current_menu.draw_menu()
                Logger.log_message("Entered Credits Menu")

            case StateType.IN_QUIT_MENU:
                self.running = False
                Logger.log_message("Entered Quit Menu")

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                state_changed = self.current_menu.check_menu_buttons()
                if state_changed != None:
                    self.state_manager.set_game_state(state_changed)
                    self.draw()
        
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
            self.draw_utils()
            self.update()
        pygame.quit()

# Utils
# Wynieśc do klasy UtilityDraw
    def draw_fps(self):
        # Create fps_text Text object:
        fps = int(self.clock.get_fps())
        fps = "{:.1f}".format(fps)
        fps_text = Text(text=fps, size=15, color=C_WHITE)
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
            text = Button(f"{chr(pos_char)}", 15, C_GREEN, None)
            text.draw(self.main_surface, pos)
            pos_char += 1
