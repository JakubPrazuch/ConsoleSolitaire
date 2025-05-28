from time import time


class MoveCounter:
    def __init__(self) -> None:
        self.moves = 0

    def display(self) -> str:
        if self.moves < 1000000:
            lenght = len(str(self.moves))
            return f"| {self.moves}{' ' * (7 - lenght)}|"
        else:
            return "| XD     |"


class Timer:
    def start(self) -> None:
        self.start_time = int(time())

    def stop(self) -> str:
        self.end_time = int(time())
        self.time_ = self.end_time - self.start_time

        hours = self.time_ // 3600
        minutes = (self.time_ % 3600) // 60
        seconds = self.time_ % 60

        return f"{hours:02}:{minutes:02}:{seconds:02}"
