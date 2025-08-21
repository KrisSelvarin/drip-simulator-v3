# for menu interface
from drip.constant import EXIT

class MenuHandler:

    @staticmethod
    def startup():
        """Startup Header"""
        print(f'\n=== DRIP SIMULATOR v3 ===\n')

    @staticmethod
    def summary():
        """Summary Header"""
        print(f'\n=== Simulation Results ===')

    @classmethod
    def menu(cls, market):
        print('Select a Stock:')
         # sort by ticker
        sorted_stocks = sorted(market.stocks, key = lambda x: x.ticker)

        # adding the sorted stocks in a dict
        menu = {i: stock for i, stock in enumerate(sorted_stocks, start=1)}

        # add exit in menu
        menu[len(sorted_stocks) + 1] = EXIT

        # print dict
        for key, value in menu.items():
            if value == EXIT:
                print(f"[{key}] {EXIT}")
            else:
                print(f"[{key}] {value.name} ({value.ticker})")

        return menu