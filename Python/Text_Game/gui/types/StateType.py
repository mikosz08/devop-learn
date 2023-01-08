from enum import Enum


class StateType(Enum):
    IN_MAIN_MENU = 1
    IN_START_MENU = 2
    IN_CREDITS_MENU = 3
    IN_CHARACTER_CREATION = 4
    IN_GAME = 5
    IN_QUIT_MENU = 6
