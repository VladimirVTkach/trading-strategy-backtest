from model.strategy import Strategy


class HoldStrategy(Strategy):
    def run(self, candlesticks, initial_balance):
        buy_price = candlesticks[0].open
        asset_amount = initial_balance / float(buy_price)

        balance_history = [initial_balance]
        for candlestick in candlesticks[1:]:
            current_price = candlestick.close
            current_balance = asset_amount * float(current_price)
            balance_history.append(current_balance)

        return balance_history
