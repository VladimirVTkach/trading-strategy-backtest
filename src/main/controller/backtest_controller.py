class BacktestController:
    def __init__(self, template_engine):
        self._template_engine = template_engine

    async def get_backtest_form(self, request):
        return self._template_engine.TemplateResponse("backtest.html",
                                                      {"request": request})

    async def get_backtest_result(self,
                                  symbol: str,
                                  interval: str,
                                  start_date: str):
        return "ok"
