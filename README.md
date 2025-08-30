# DRIP Simulator v3  

A modular **Dividend Reinvestment Plan (DRIP) Simulator** for PSEI REIT stocks.  
Simulates dividend payouts, reinvestment, and portfolio growth over time with CSV export and graph visualization.  

## Features  
- Menu-driven interface for selecting stocks  
- Modular structure (`stock`, `market`, `csv_handler`, `input_handler`, `menu_handler`, `visuals`)  
- Dividend reinvestment simulation with configurable **monthly investment** and **years**  
- Automatic **CSV logging** of simulation results  
- Graphs:  
  - Portfolio overview (growth curve)  
  - Dividend growth (bar chart)  
  - Portfolio composition (dividends vs. capital)  
- Dark mode styled plots  

## Example Run  
```bash
=== DRIP SIMULATOR v3 ===

== MAIN MENU ==
[1] AyalaLand REIT Inc. (AREIT)
[2] CITICORE ENERGY REIT CORP. (CREIT)
[3] RL COMMERCIAL REIT INC. (RCR)
[4] STOCKS INFO
[5] EXIT
Selection: 2

Monthly Investment: ₱4000
Investment Duration (Years): 5
```

**Simulation Results**  
```bash
Total Shares:               74,000 shares
Total Shares Amount:        ₱   272,320.00
Total Dividends Earned:     ₱    31,404.65
Remaining Buying Power:     ₱     4,803.38
```

Generates CSV file:  
```
data/CREIT_5Y_4000_0.csv
```

Sample output (first rows):  

| Year | Pay-out | Dividends | Shares | Amount   | Buying Power |
|------|---------|-----------|--------|----------|--------------|
| 1    | 1       | 151.52    | 3000   | 11040.00 | 1111.52      |
| 1    | 2       | 303.05    | 6000   | 22080.00 | 2374.57      |
| 1    | 3       | 454.57    | 9000   | 33120.00 | 3789.14      |

## Requirements  
- Python 3.9+  
- Libraries: `numpy`, `pandas`, `matplotlib`, `scipy`  

Install with:  
```bash
pip install -r requirements.txt
```

## Run  
```bash
python menu.py
```

## Notes  
- v1 (procedural) and v2 (OOP) are archived in separate repos  
- v3: modular, professional structure with CSV + visualization  
- This is a **learning project** — code may be improved further as skills grow  
