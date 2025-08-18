# for log
from drip.csv_handler import CSVWriter
# collection of stocks

class Market:
    def __init__(self):
        self.stocks = []

    def add_stock(self, stock):
        """Appends instantiated stocks to a list"""
        self.stocks.append(stock)

    def stocks_info(self):
        """Cycle through stocks list"""
        for stock in self.stocks:
            print(f'{stock.ticker}')

    def start_simulations(self, stock, year, monthly_investment):
        """Simulate monthly looping with dividend reinvestment"""
        # reset values
        stock.reset_values()

        total_months = year * 12
        months_per_payout = 12 // stock.frequency

        # csv setup
        filename = f"data/{stock.ticker.upper()}_{year}Y_{str(monthly_investment).replace('.', '_')}.csv"
        header = ['Year', 'Pay-out', 'Dividends', 'Shares', 'Buying Power']
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
