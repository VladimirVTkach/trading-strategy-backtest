from fastapi import FastAPI
from binance import AsyncClient
from service.market_data_service import MarketDataService
from controller.market_data_controller import MarketDataController

client = AsyncClient()
market_data_service = MarketDataService(client)
market_data_controller = MarketDataController(market_data_service)

app = FastAPI()


@app.get("/candlesticks/historic/{symbol}/{market_type}/{interval}/{start_date}")
async def get_historical_candlesticks(symbol, market_type, interval, start_date):
    return await market_data_controller.get_historical_candlesticks(symbol=symbol,
                                                                    market_type=market_type,
                                                                    interval=interval,
                                                                    start_date=start_date)


@app.get("/candlesticks/current/{symbol}/{market_type}/{interval}")
async def get_current_candlestick(symbol, market_type, interval):
    return await market_data_controller.get_current_candlestick(symbol=symbol,
                                                                market_type=market_type,
                                                                interval=interval)
