# main simulation flow of DRIP

from drip.input_handler import InputHandler
from drip.market import Market
from drip.menu_handler import MenuHandler
from drip.visuals import Visuals
from drip.constant import PESOS



class Simulate:

    @staticmethod
    def result_simulations(selected_stock):
        """Runs the Dividend Reinvestment Plan (DRIP) simulation flow"""
        monthly_investment = InputHandler.get_positive_float(f"\nMonthly Investment: {PESOS}")
        year = InputHandler.get_positive_int(f"Investment Duration (Years): ")

        # Start Simulations
        results, filename = Market.start_simulations(selected_stock, year, monthly_investment)

        # results
        MenuHandler.summary()
        Market.stock_info(selected_stock)
        print(f"Total Shares:               {results['total shares']:,} shares")
        print(f"Total Shares Amount:        {PESOS}{results['shares amount']:>12,.2f}")
        print(f"Total Dividends Earned:     {PESOS}{results['total dividends']:>12,.2f}")
        print(f"Remaining Buying Power:     {PESOS}{results['remaining bp']:>12,.2f}")

        # graph
        Visuals.graph(filename, InputHandler.response('Show Graph (Y|N)? '))