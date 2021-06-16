import numpy as np
from model.strategy import Strategy


class MeanPriceBasedStrategy(Strategy):
    def run(self, candlesticks, initial_balance):
        current_balance = initial_balance
        asset_amount = 0

        is_in_position = False

        balance_history = [initial_balance]
        previous_prices = []

        for candlestick in candlesticks:
            current_price = float(candlestick.close)

            if len(previous_prices) < 10:
                previous_prices.append(current_price)
                continue

            mean_price = np.mean(previous_prices)

            if is_in_position:
                if current_price < mean_price:
                    current_balance = asset_amount * current_price
                    balance_history.append(current_balance)
                    is_in_position = False
            else:
                if current_price > mean_price:
                    asset_amount = current_balance / current_price
                    current_balance = 0
                    is_in_position = True

            previous_prices.pop(0)
            previous_prices.append(current_price)

        return balance_history
