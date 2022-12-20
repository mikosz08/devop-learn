from utils.Log import Log

class Logger(Log):

    logs = []

    @classmethod
    def log_message(cls, message) -> str():
        Logger.append_log(cls, f"|LOG|{Log(message)}")

    @classmethod
    def log_value(cls, value) -> str():
        Logger.append_log(cls, f"|VALUE|{Log(value)}")

    @classmethod
    def print_logs(cls):
        for log in Logger.logs:
            print(f"{log}", end=f'\n')

    def append_log(self, log):
        Logger.logs.append(f"@\n{log}")
