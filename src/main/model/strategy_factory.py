from model.hold_strategy import HoldStrategy


class StrategyFactory:
    def __init__(self):
        self._strategies = {"hold": HoldStrategy()}

    def get_strategy(self, name):
        return self._strategies[name]
