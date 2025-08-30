# stocks instantiation
from drip.stock import Stock
from drip.market import Market

class Setup():

    @staticmethod
    def create_market():
        # instantiate
        creit = Stock('CITICORE ENERGY REIT CORP.', 'CREIT', 3.68, 5.49, 1000, 4)
        rcr = Stock('RL COMMERCIAL REIT INC.', 'RCR', 7.90, 5.22, 100, 4)
        areit = Stock('AyalaLand REIT Inc.', 'AREIT', 42.60, 5.41, 100, 4)

        # add to market list
        market = Market()
        market.add_stock(creit)
        market.add_stock(rcr)
        market.add_stock(areit)

        return market