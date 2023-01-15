from enum import Enum
from gui.types.StateType import StateType


class ButtonType(Enum):
    # Main Menu:
    START_BUTTON = ("Start", StateType.IN_START_MENU, 45)
    QUIT_BUTTON = ("Quit", StateType.IN_QUIT_MENU, 35)
    CREDITS_BUTTON = ("Credits", StateType.IN_CREDITS_MENU, 30)

    # Start Menu
    NEW_GAME_BUTTON = ("New Game", StateType.EMPTY_STATE, 45)
    CONTINUE_BUTTON = ("Continue", StateType.EMPTY_STATE, 40)
    BACK_BUTTON = ("Back", StateType.IN_MAIN_MENU, 35)


MAIN_MENU_BUTTONS = [
    ButtonType.START_BUTTON.value,
    ButtonType.CREDITS_BUTTON.value,
    ButtonType.QUIT_BUTTON.value
]

START_MENU_BUTTONS = [
    ButtonType.CONTINUE_BUTTON.value,
    ButtonType.NEW_GAME_BUTTON.value,
    ButtonType.BACK_BUTTON.value
]

CREDITS_MENU_BUTTONS = [
    ButtonType.BACK_BUTTON.value
]
