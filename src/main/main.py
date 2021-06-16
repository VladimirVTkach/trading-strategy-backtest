from binance import AsyncClient
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from controller.backtest_controller import BacktestController
from service.market_data_service import MarketDataService
from service.backtest_service import BacktestService
from model.strategy_factory import StrategyFactory

client = AsyncClient()
market_data_service = MarketDataService(client)

strategy_factory = StrategyFactory()
backtest_service = BacktestService(market_data_service, strategy_factory)

templates_engine = Jinja2Templates(directory="../resources/templates")
backtest_controller = BacktestController(template_engine=templates_engine, backtest_service=backtest_service)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_backtest_form(request: Request):
    return await backtest_controller.get_backtest_form(request)


@app.post("/backtest/run/")
async def get_backtest_result(symbol: str = Form(...),
                              interval: str = Form(...),
                              start_date: str = Form(...),
                              initial_balance: int = Form(...),
                              strategy: str = Form(...)):
    return await backtest_controller.get_backtest_result(symbol=symbol,
                                                         interval=interval,
                                                         start_date=start_date,
                                                         initial_balance=initial_balance,
                                                         strategy=strategy)
