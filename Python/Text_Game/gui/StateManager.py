from utils.Logger import Logger


class StateManager:

    def __init__(self, initial_state) -> None:
        self.game_state = initial_state

    def set_game_state(self, state):
        self.game_state = state
        Logger.log_message(f"State changed to [{state}]")

    def get_game_state(self):
        return self.game_state
