import time
import datetime
from model.time_interval import TimeInterval
from starlette.responses import FileResponse


class BacktestController:
    def __init__(self, template_engine, backtest_service):
        self._template_engine = template_engine
        self._backtest_service = backtest_service

    async def get_backtest_form(self, request):
        return self._template_engine.TemplateResponse("backtest.html",
                                                      {"request": request})

    async def get_backtest_result(self,
                                  symbol: str,
                                  interval: str,
                                  start_date: str,
                                  initial_balance: int,
                                  strategy: str):
        start_date_timestamp = int(time.mktime(datetime.datetime.strptime(start_date, "%d-%m-%Y").timetuple()))
        time_interval = self._get_time_interval(interval)

        filename = await self._backtest_service.get_backtest_result(symbol=symbol,
                                                                    start_date=start_date_timestamp,
                                                                    initial_balance=initial_balance,
                                                                    interval=time_interval,
                                                                    strategy=strategy)
        return FileResponse(filename,
                            media_type='application/octet-stream',
                            filename=filename)

    def _get_time_interval(self, interval):
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
