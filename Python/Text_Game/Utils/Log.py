
import time

message = str()


class Log():
    def __init__(self, log) -> None:
        timestamp = time.ctime()
        self.message = f"|{timestamp}|{log}"

    def __str__(self) -> str:
        return self.message
