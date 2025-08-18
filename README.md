# DRIP Simulator v3

A simple, modular **Dividend Reinvestment Plan (DRIP) simulator** for tracking single or multiple stocks. Outputs yearly/quarterly dividends and share accumulation to CSV.

## Features
- Modular Python code structure  
- CSV logging of simulation results  
- Multi-stock tracking  
- Future support for FX rates, fees, and taxes  

## Folder Structure
- `drip/` — Python modules  
- `data/` — CSV outputs  
- `logs/` — Placeholder for logs  

## Quick Example
```python
from drip.stock import Stock
from drip.market import Market

market = Market()
creit = Stock('CITICORE ENERGY REIT CORP.', 'CREIT', 3.68, 5.49, 1000, 4)
market.add_stock(creit)

results = market.start_simulations(creit, year=5, monthly_investment=5000)
print(results)
