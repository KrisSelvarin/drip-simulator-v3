from drip.stock import Stock
from drip.market import Market
from drip.menu_handler import MenuHandler
from drip.input_handler import InputHandler
from drip.constant import PESOS, EXIT

# instantiate
creit = Stock('CITICORE ENERGY REIT CORP.', 'CREIT', 3.68, 5.49, 1000, 4)
rcr = Stock('RL COMMERCIAL REIT INC.', 'RCR', 7.90, 5.22, 100, 4)
areit = Stock('AyalaLand REIT Inc.', 'AREIT', 42.60, 5.41, 100, 4)

# add to market list
market = Market()
market.add_stock(creit)
market.add_stock(rcr)
market.add_stock(areit)

# Start up 
MenuHandler.startup()

# Menu Dictionary
menu = MenuHandler.menu(market)

# Select Stock to Simulate
selected_stock = InputHandler.choose_from_list("Selection: ", menu)
if selected_stock == EXIT:
    exit()

# User Input for Years and Monthly Investment
print()
monthly_investment = InputHandler.get_positive_float(f"Monthly Investment: {PESOS}")
year = InputHandler.get_positive_int(f"Investment Duration (Years): ")

# Start Simulations
results = market.start_simulations(selected_stock, year, monthly_investment)

# results
MenuHandler.summary()
market.stock_info(selected_stock)
print(f"Total Shares:               {results['total shares']:,} shares")
print(f"Total Shares Amount:        {PESOS}{results['shares amount']:>12,.2f}")
print(f"Total Dividends Earned:     {PESOS}{results['total dividends']:>12,.2f}")
print(f"Remaining Buying Power:     {PESOS}{results['remaining bp']:>12,.2f}")
print()


