from Utils.Logger import Logger
from Utils.clear_screen import cls
from brain.Game import Game

if __name__ == "__main__":
    cls()
    Logger.log_message("Program starts")
    Game()
    Logger.log_message("Program ends")
    Logger.print_logs()
