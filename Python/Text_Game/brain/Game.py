from gui.Gui import Gui
from gui.game_settings import *


class Game():

    def __init__(self) -> None:
        Gui(WIN_WIDTH, WIN_HEIGHT, WIN_TITLE, FPS)
