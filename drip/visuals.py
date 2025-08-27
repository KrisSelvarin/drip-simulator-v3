# for graph generation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import gridspec
from scipy.interpolate import make_interp_spline

class Visuals:
    
    @staticmethod
    def graph(filename):
        """Generates Graph"""
        data = pd.read_csv(filename)

        # 3-PANEL GRAPH (dark mode)
        fig = plt.figure(figsize=(12,8), facecolor="#1e1e1e")
        gs = gridspec.GridSpec(2, 2, figure=fig)

        # runtime config
        plt.rcParams.update()

        # ----------------------- main graph --------------------------------------
        ax_main = fig.add_subplot(gs[0, :])     # first row span 2 columns
        x_main = data.index
        y_main = data['Amount']

        x_smooth = np.linspace(x_main.min(), x_main.max(), 300)
        slp = make_interp_spline(x_main, y_main, k=2)     # quadratic
        y_smooth = slp(x_smooth)

        ax_main.plot(x_smooth, y_smooth)
        ax_main.scatter(x_main, y_main, zorder=3, color='red', marker='o', s=4)
        ax_main.set_title('PORTFOLIO OVERVIEW', fontweight='bold')

        x_main_labels = [f'Q{val}' for val in data['Pay-out']]
        ax_main.set_xticks(x_main, labels=x_main_labels, fontsize=8)

        for year in data['Year'].unique():
            position = x_main[data['Year'] == year]
            mid = position.values.mean()
            Year = f'Year {year}'
            ax_main.text(
                mid, -0.1, Year,
                ha='center', va='top',
                transform=ax_main.get_xaxis_transform()
            )

        ax_main.yaxis.set_major_formatter(
            FuncFormatter(lambda x, _: f'{x:,.0f}')
        )
        ax_main.set_ylabel('AMOUNT (PHP)', fontweight='semibold')

        # ----------------------- dividends per quarter --------------------------------------
        ax_1 = fig.add_subplot(gs[1, 0])    # 2nd row 1st column
        ax_1.bar(data.index, data['Dividends'])
        ax_1.set_title('DIVIDEND GROWTH', fontweight='bold')

        ax_1_labels = [f'Q{val}' for val in data['Pay-out']]
        ax_1.set_xticks(data.index, ax_1_labels, fontsize=7)

        for year in data['Year'].unique():
            position = data.index[data['Year'] == year]
            mid = position.values.mean()
            Year = f'Year {year}'
            ax_1.text(
                mid, -0.1, Year,
                ha='center', va='top',
                transform=ax_1.get_xaxis_transform()
            )

        ax_1.yaxis.set_major_formatter(
            FuncFormatter(lambda x, _: f'{x:,.0f}')
        )
        ax_1.set_ylabel('DIVIDENDS (PHP)', fontweight='semibold')

        # ----------------------- portfolio compostion --------------------------------------
        ax_2 = fig.add_subplot(gs[1,1])     # 2nd row 2nd column

        # pie chart values
        div = data.iloc[-1, data.columns.get_loc('Dividends')]
        capital = data.iloc[-1, data.columns.get_loc('Amount')] - div
        sizes = [div, capital]
        labels = ['Dividends', 'Capital Growth']

        ax_2.pie(sizes, labels=labels, autopct='%1.2f%%', startangle=90)
        ax_2.set_title('PORTFOLIO COMPOSITION', fontweight='bold')

        
        # show graph
        plt.tight_layout(pad=2.0)
        plt.show()