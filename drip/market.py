from drip.csv_handler import CSVWriter
from drip.constant import PESOS
# collection of stocks

class Market:
    def __init__(self):
        self.stocks = []
        self.f = {12:'Monthly', 4:'Quarterly', 2:'Bi-Annually', 1:'Annually'}

    def add_stock(self, stock):
        """Appends instantiated stocks to a list"""
        self.stocks.append(stock)

    def all_stocks(self, stock):
        """Cycle through stocks list"""
        for stock in self.stocks:
            freq = self.f[stock.frequency]
            print(
                f'\n{stock.name} {stock.ticker}\n'
                f'Price per Share:              {PESOS}{stock.price:,.2f}\n'
                f'Dividend Yield (Indicated):   {stock.div_yield}%\n'
                f'Payout Frequency:             {freq}\n'
                f'Dividend per Share:           {PESOS}{stock.div_per_share:,.2f}'
            )
    
    def stock_info(self, stock):
        """Info function for the selected stock"""
        freq = self.f[stock.frequency]
        print(
            f'\n{stock.name} {stock.ticker}\n'
            f'Price per Share:              {PESOS}{stock.price:,.2f}\n'
            f'Dividend Yield (Indicated):   {stock.div_yield}%\n'
            f'Payout Frequency:             {freq}\n'
            f'Dividend per Share:           {PESOS}{stock.div_per_share:,.2f}\n'
        )

    def start_simulations(self, stock, year, monthly_investment):
        """Simulate monthly looping with dividend reinvestment"""
        # reset values
        stock.reset_values()

        total_months = year * 12
        months_per_payout = 12 // stock.frequency

        # csv setup
        filename = CSVWriter.csv_filename(stock, year, monthly_investment)
        header = ['Year', 'Pay-out', 'Dividends', 'Shares', 'Amount', 'Buying Power']
        CSVWriter.open(filename, header)    # open csv file


        for month in range(total_months):
            stock.deposit(monthly_investment)
            stock.buy_lots()

            if (month + 1) % (months_per_payout) == 0:
                div = stock.add_dividends()

                year_num = (month // 12) + 1
                payout_num = ((month % 12) // months_per_payout) + 1

                # streams row directly to csv
                CSVWriter.write_row({
                    "Year": year_num,
                    "Pay-out": payout_num,
                    "Dividends": round(div, 2),
                    "Shares": stock.total_shares,
                    "Amount": stock.total_shares * stock.price,
                    "Buying Power": round(stock.buying_power, 2),

                })

        # closes csv file
        CSVWriter.close()

        # return for summary
        return {
            'total shares': stock.total_shares,
            'shares amount': stock.total_shares * stock.price,
            'total dividends': stock.total_dividends,
            'remaining bp': stock.buying_power,
        }
