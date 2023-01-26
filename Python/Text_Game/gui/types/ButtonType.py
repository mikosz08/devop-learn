from enum import Enum
from gui.types.StateType import StateType


class ButtonType(Enum):
    # Main Menu:
    START_BUTTON = ("Start", StateType.IN_START_MENU, 45)
    QUIT_BUTTON = ("Quit", StateType.IN_QUIT_MENU, 35)
    CREDITS_BUTTON = ("Credits", StateType.IN_CREDITS_MENU, 30)

    # Start Menu
    NEW_GAME_BUTTON = ("New Game", StateType.IN_NEW_GAME_MENU, 45)
    CONTINUE_BUTTON = ("Continue", StateType.IN_CONTINUE_MENU, 40)
    
    # New Game Menu
    DONE_BUTTON = ("Done", StateType.IN_GAME, 35)
    
    BACK_TO_MAIN_MENU_BUTTON = ("Back", StateType.IN_MAIN_MENU, 35)
    BACK_TO_START_MENU_BUTTON = ("Back", StateType.IN_START_MENU, 35)
        

MAIN_MENU_BUTTONS = [
    ButtonType.START_BUTTON.value,
    ButtonType.CREDITS_BUTTON.value,
    ButtonType.QUIT_BUTTON.value
]

START_MENU_BUTTONS = [
    ButtonType.CONTINUE_BUTTON.value,
    ButtonType.NEW_GAME_BUTTON.value,
    ButtonType.BACK_TO_MAIN_MENU_BUTTON.value
]

CREDITS_MENU_BUTTONS = [
    ButtonType.BACK_TO_MAIN_MENU_BUTTON.value
]

NEW_GAME_BUTTONS = [
    ButtonType.DONE_BUTTON.value,
    ButtonType.BACK_TO_START_MENU_BUTTON.value
]