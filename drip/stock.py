# for stocks

class Stock:
    def __init__(self, name, ticker, price, div_yield, board_lot, frequency):
        self.name = name.upper()
        self.ticker = ticker.upper()
        self.price = price
        self.div_yield = div_yield
        self.board_lot = board_lot
        self.frequency = frequency
        self.div_per_share = (price * (div_yield / 100)) / frequency

        # state
        self.buying_power = 0
        self.total_shares = 0
        self.total_dividends = 0

    def deposit(self, deposit):
        """Add monthly investment to buying power"""
        self.buying_power += deposit

    def buy_lots(self):
        """Buy maximum number of lots possible"""
        lot_price = self.board_lot * self.price
        lots_bought = int(self.buying_power // lot_price)
        if lots_bought > 0:
            shares_bought = lots_bought * self.board_lot
            self.total_shares += shares_bought
            self.buying_power -= (lots_bought * lot_price)     # remaining buying power
            return shares_bought
        return 0
    
    def add_dividends(self):
        """Add dividends to buying power"""
        dividends = self.div_per_share * self.total_shares
        self.buying_power += dividends
        self.total_dividends += dividends       # tracks total dividends paid by stock
        return dividends
    
    def reset_values(self):
        """Resets state values"""
        self.buying_power = 0
        self.total_shares = 0
        self.total_dividends = 0