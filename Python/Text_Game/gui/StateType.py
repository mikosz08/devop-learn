from enum import Enum


class StateType(Enum):
    IN_MAIN_MENU="in_main_menu"
    IN_START_MENU="in_start_menu"
    IN_CHARACTER_CREATION="in_character_creation"
    IN_GAME="in_game"
    QUIT="quit"