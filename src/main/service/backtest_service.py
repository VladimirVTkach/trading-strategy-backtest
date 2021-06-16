from model.market_type import MarketType
from model.time_interval import TimeInterval

import matplotlib.pyplot as plt


class BacktestService:
    def __init__(self, market_data_service, strategy_factory):
        self._market_data_service = market_data_service
        self._strategy_factory = strategy_factory
        self._current_file_index = 1

    async def get_backtest_result(self,
                                  symbol: str,
                                  start_date: int,
                                  initial_balance: int,
                                  interval: TimeInterval,
                                  strategy: str):
        candlesticks = await self._market_data_service.get_historical_candlesticks(symbol=symbol,
                                                                                   market_type=MarketType.SPOT,
                                                                                   interval=interval,
                                                                                   start_date=start_date)
        strategy = self._strategy_factory.get_strategy(strategy)
        balance_history = strategy.run(candlesticks=candlesticks,
                                       initial_balance=initial_balance)

        plt.clf()
        plt.plot(balance_history)

        filename = f'balance_history_{self._current_file_index}.png'
        plt.savefig(filename)

        self._current_file_index += 1

        return filename
