# collection of stocks
from drip.simulations import simulate

class Market:
    stocks = []

    @classmethod
    def add_stock(cls, stock):
        """Appends instantiated stocks to a list"""
        cls.stocks.append(stock)

    @classmethod
    def stocks_info(cls):
        """Cycle through stocks list"""
        for stock in cls.stocks:
            print(f'{stock.ticker}')

    @classmethod
    def start_simulations(cls, selected_stock, year, monthly_investment):
        """Start DRIP Simulation"""
        return simulate(selected_stock, year, monthly_investment)