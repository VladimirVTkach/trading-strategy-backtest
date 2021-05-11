from enum import Enum


class CandlestickColor(Enum):
    GREEN = 0
    RED = 1


class Candlestick:
    open_time: int
    close_time: int
    open: float
    close: float
    high: float
    low: float
    volume: float

    def __init__(self,
                 open_time: int,
                 close_time: int,
                 open: float,
                 close: float,
                 high: float,
                 low: float,
                 volume: float):
        self.open_time = open_time
        self.close_time = close_time
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.volume = volume

    def get_height(self):
        return self.open - self.close

    def get_absolute_height(self):
        return abs(self.open - self.close)

    def get_color(self):
        if self.close >= self.open:
            return CandlestickColor.GREEN
        else:
            return CandlestickColor.RED
