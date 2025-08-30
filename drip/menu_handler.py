# for menu interface
from drip.constant import EXIT, INFO

class MenuHandler:

    @staticmethod
    def startup():
        """Startup Header"""
        print(f'\n=== DRIP SIMULATOR v3 ===')

    @staticmethod
    def summary():
        """Summary Header"""
        print(f'\n=== Simulation Results ===')

    @staticmethod
    def main_menu(market):
        print('\n== MAIN MENU ==')
         # sort by ticker
        sorted_stocks = sorted(market.stocks, key = lambda x: x.ticker)

        # adding the sorted stocks in a dict
        menu = {i: stock for i, stock in enumerate(sorted_stocks, start=1)}

        # add info and exit in menu
        menu[len(sorted_stocks) + 1] = INFO
        menu[len(sorted_stocks) + 2] = EXIT

        # print dict
        for key, value in menu.items():
            if value == EXIT:
                print(f"[{key}] {EXIT}")
            elif value == INFO:
                print(f"[{key}] {INFO}")
            else:
                print(f"[{key}] {value.name} ({value.ticker})")

        # returns dict
        return sorted_stocks, menu