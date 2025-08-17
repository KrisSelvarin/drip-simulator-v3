# monthly simulation loop

def simulate(stock, year, monthly_investment):
    """Simulate monthly looping with dividend reinvestment"""
    # reset values
    stock.reset_values()

    total_months = year * 12
    months_per_payout = 12 // stock.frequency

    for month in range(total_months):
        stock.deposit(monthly_investment)
        stock.buy_lots()

        if (month + 1) % (months_per_payout) == 0:
            stock.add_dividends()

    return {
        'total shares': stock.total_shares,
        'shares amount': stock.total_shares * stock.price,
        'total dividends': stock.total_dividends,
        'remaining bp': stock.buying_power,
    }
