from model.hold_strategy import HoldStrategy
from model.mean_price_based_strategy import MeanPriceBasedStrategy


class StrategyFactory:
    def __init__(self):
        self._strategies = {"hold": HoldStrategy(),
                            "mean_price_based": MeanPriceBasedStrategy()}

    def get_strategy(self, name):
        return self._strategies[name]
