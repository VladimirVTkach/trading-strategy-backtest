from service.market_data_service import MarketDataService
from model.market_type import MarketType
from model.time_interval import TimeInterval


class MarketDataController:
    def __init__(self, market_data_service: MarketDataService):
        self._market_data_service = market_data_service

    async def get_historical_candlesticks(self,
                                          symbol: str,
                                          market_type: str,
                                          interval: str,
                                          start_date: int):
        parsed_market_type = self._parse_market_type(market_type)
        parsed_interval = self._parse_interval(interval)

        historical_candlesticks = await self._market_data_service.get_historical_candlesticks(symbol=symbol,
                                                                                              market_type=parsed_market_type,
                                                                                              interval=parsed_interval,
                                                                                              start_date=start_date)
        return historical_candlesticks

    async def get_current_candlestick(self,
                                      symbol: str,
                                      market_type: str,
                                      interval: str):
        parsed_market_type = self._parse_market_type(market_type)
        parsed_interval = self._parse_interval(interval)

        current_candlestick = await self._market_data_service.get_current_candlestick(symbol=symbol,
                                                                                      market_type=parsed_market_type,
                                                                                      interval=parsed_interval)
        return current_candlestick

    def _parse_market_type(self, market_type):
        if market_type == "spot":
            return MarketType.SPOT
        elif market_type == "futures":
            return MarketType.FUTURES
        else:
            return None

    def _parse_interval(self, interval):
        if interval == "1d":
            return TimeInterval.ONE_DAY
        elif interval == "1h":
            return TimeInterval.ONE_HOUR
        elif interval == "6h":
            return TimeInterval.SIX_HOUR
        elif interval == "15m":
            return TimeInterval.FIFTEEN_MINUTES
        elif interval == "1m":
            return TimeInterval.ONE_MINUTE
        else:
            return None
