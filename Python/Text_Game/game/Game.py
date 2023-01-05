from gui.Gui import Gui
from utils.Logger import Logger


class Game():

    def __init__(self) -> None:
        Logger.log_message("Game loop starts")
        Gui().main_loop()
