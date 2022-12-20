from utils.Logger import Logger
from utils.clear_screen import cls
from brain.Game import Game

if __name__ == "__main__":
    cls()
    Game()
    Logger.log_message("[Program ends ..]")
    Logger.print_logs()
