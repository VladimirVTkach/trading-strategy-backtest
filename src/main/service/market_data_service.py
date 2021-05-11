from typing import List
from binance import AsyncClient
from binance.enums import HistoricalKlinesType
from binance.enums import KLINE_INTERVAL_1DAY, KLINE_INTERVAL_1HOUR, KLINE_INTERVAL_6HOUR, KLINE_INTERVAL_15MINUTE, \
    KLINE_INTERVAL_1MINUTE
from model.candlestick import Candlestick
from model.market_type import MarketType
from model.time_interval import TimeInterval


class MarketDataService:
    def __init__(self, binance_client: AsyncClient):
        self._binance_client = binance_client

    async def get_historical_candlesticks(self,
                                          symbol: str,
                                          market_type: MarketType,
                                          interval: TimeInterval,
                                          start_date: int) -> List[Candlestick]:
        kline_interval = self._get_kline_interval(interval)
        historical_klines_type = self._get_historical_klines_type(market_type)

        historical_klines = await self._binance_client.get_historical_klines(symbol=symbol,
                                                                             interval=kline_interval,
                                                                             start_str=start_date,
                                                                             klines_type=historical_klines_type)

        historical_candlesticks = [self._build_candlestick(item) for item in historical_klines]

        return historical_candlesticks

    async def get_current_candlestick(self,
                                      symbol: str,
                                      market_type: MarketType,
                                      interval: TimeInterval) -> Candlestick:
        kline_interval = self._get_kline_interval(interval)

        if market_type == MarketType.SPOT:
            klines = await self._binance_client.get_klines(symbol=symbol,
                                                           interval=kline_interval,
                                                           limit=1)
        else:
            klines = await self._binance_client.futures_klines(symbol=symbol,
                                                               interval=kline_interval,
                                                               limit=1)

        return self._build_candlestick(klines[0])

    def _get_kline_interval(self, interval: TimeInterval):
        if interval == TimeInterval.ONE_DAY:
            return KLINE_INTERVAL_1DAY
        elif interval == TimeInterval.ONE_HOUR:
            return KLINE_INTERVAL_1HOUR
        elif interval == TimeInterval.SIX_HOUR:
            return KLINE_INTERVAL_6HOUR
        elif interval == TimeInterval.FIFTEEN_MINUTES:
            return KLINE_INTERVAL_15MINUTE
        elif interval == TimeInterval.ONE_MINUTE:
            return KLINE_INTERVAL_1MINUTE

    def _get_historical_klines_type(self, market_type: MarketType):
        if market_type == MarketType.SPOT:
            return HistoricalKlinesType.SPOT
        return HistoricalKlinesType.FUTURES

    def _build_candlestick(self, kline):
        return Candlestick(open_time=kline[0],
                           close_time=kline[6],
                           open=kline[1],
                           close=kline[4],
                           high=kline[2],
                           low=kline[3],
                           volume=kline[5])
