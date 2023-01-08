import pygame
from gui.MainMenu import MainMenu
from gui.StateManager import StateManager
from gui.Text import Text
from utils.Logger import Logger
from gui.types.StateType import StateType
from gui.game_settings import *
from gui.types.ButtonType import ButtonType


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

    def check_buttons(self):
        match self.state_manager.get_game_state():
            case StateType.IN_MAIN_MENU:

                for button in self.main_menu.get_menu_buttons():
                    pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()[0] == 1
                    collision_detected = button.rect.collidepoint(pos)
                    if collision_detected and mouse_pressed:
                        sm = self.state_manager
                        match button.tag:
                            case ButtonType.START_BUTTON.value:
                                sm.set_game_state(StateType.IN_START_MENU)
                                self.draw()
                            case ButtonType.CREDITS_BUTTON.value:
                                sm.set_game_state(StateType.IN_CREDITS_MENU)
                                self.draw()
                            case ButtonType.QUIT_BUTTON.value:
                                sm.set_game_state(StateType.IN_QUIT)
                                self.draw()

            case StateType.IN_START_MENU:
                pass
            case StateType.IN_CREDITS_MENU:
                pass
            case StateType.IN_GAME:
                pass

    def draw(self):
        game_state = self.state_manager.get_game_state()
        match game_state:
            case StateType.IN_MAIN_MENU:
                self.main_menu = MainMenu(self.main_surface).draw()
                Logger.log_message("Entered Main Menu")

            case StateType.IN_START_MENU:
                self.main_surface.fill(C_BLACK)
                Logger.log_message("Entered Start Menu")

            case StateType.IN_CREDITS_MENU:
                self.main_surface.fill(C_RED)
                Logger.log_message("Entered Credits Menu")

            case StateType.IN_QUIT:
                self.running = False
                Logger.log_message("Entered Quit Menu")

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

    def draw_utils(self):
        self.draw_window_positions()
        self.draw_fps()

    def update(self):
        self.main_display.update()
        self.clock.tick(self.fps)

    def main_loop(self):
        while (self.running):
            self.check_events()
            self.check_buttons()
            self.draw_utils()
            self.update()
        pygame.quit()
