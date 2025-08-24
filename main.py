from drip.stock import Stock
from drip.market import Market
from drip.menu_handler import MenuHandler
from drip.input_handler import InputHandler
from drip.constant import PESOS, EXIT, INFO
from drip.visuals import Visuals

# instantiate
creit = Stock('CITICORE ENERGY REIT CORP.', 'CREIT', 3.68, 5.49, 1000, 4)
rcr = Stock('RL COMMERCIAL REIT INC.', 'RCR', 7.90, 5.22, 100, 4)
areit = Stock('AyalaLand REIT Inc.', 'AREIT', 42.60, 5.41, 100, 4)

# add to market list
market = Market()
market.add_stock(creit)
market.add_stock(rcr)
market.add_stock(areit)

# Start up / greeting
MenuHandler.startup()


while True:
    # Menu Dictionary
    sorted_stocks, menu = MenuHandler.main_menu(market)

    # Select Stock to Simulate
    selected_stock = InputHandler.choose_from_list("Selection: ", menu)
    if selected_stock == EXIT:
        exit('== EXITING PROGRAM ==')
    elif selected_stock == INFO:
        Market.all_stocks(sorted_stocks)
        menu_response = InputHandler.response('Back to Main Menu (Y|N)? ')
        if menu_response == 'y':
            continue
        elif menu_response == 'Invalid Input':
            exit('INVALID INPUT: FORCE EXIT')
        else:
            exit('== EXITING PROGRAM ==')
    else:
        ### Can be put in another file
        ## Function that takes in selected_stock as arg
        # User Input for Years and Monthly Investment
        print()
        monthly_investment = InputHandler.get_positive_float(f"Monthly Investment: {PESOS}")
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
        graph_response = InputHandler.response('Show Graph (Y|N)? ')
        if graph_response == 'y':
            Visuals.graph(filename)
        elif graph_response == 'Invalid Input':
            exit('INVALID INPUT: FORCE EXIT')
        else:
            exit('== EXITING PROGRAM ==')

        # break loop
        break
