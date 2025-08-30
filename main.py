from drip.market import Market
from drip.setup import Setup
from drip.menu_handler import MenuHandler
from drip.input_handler import InputHandler
from drip.constant import EXIT, INFO
from drip.simulate import Simulate


def main():
    market = Setup.create_market()

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
            if InputHandler.response('Back to Main Menu (Y|N)? '):
                continue
            else:
                break
        else:
            Simulate.result_simulations(selected_stock)

        # program restart
        if InputHandler.response('Restart Program (Y|N)? '):
            continue
        else:
            break


# modularity
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n== PROGRAM INTERRUPTED ==')
    except Exception as e:
        print(f'\n\n== ERROR: {e} ==')
        exit('PROGRAM TERMINATED')