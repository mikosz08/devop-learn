from enum import Enum


class StateType(Enum):
    EMPTY_STATE = 0
    IN_MAIN_MENU = 1
    IN_START_MENU = 2
    IN_CREDITS_MENU = 3
    IN_NEW_GAME_MENU = 4
    IN_CONTINUE_MENU = 5
    IN_GAME = 6
    IN_QUIT_MENU = 7
    GETTING_USER_INPUT = 8
