# for graph generation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib import gridspec
from scipy.interpolate import make_interp_spline

class Visuals:
    
    @staticmethod
    def graph(filename: str, show=False):
        """Generates Graph"""
        data = pd.read_csv(filename)

        # 3-PANEL GRAPH (dark mode)
        fig = plt.figure(figsize=(13, 8), facecolor="#1e1e1e")
        gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3, width_ratios=[2.2, 1])

        # runtime config
        plt.rcParams.update({
            "axes.facecolor": "#252525",
            "axes.edgecolor": "#444444",
            "axes.labelcolor": "#dddddd",
            "xtick.color": "#cccccc",
            "ytick.color": "#cccccc",
            "text.color": "white",
            "font.family": "Segoe UI"
        })

        # ----------------------- main graph --------------------------------------
        ax_main = fig.add_subplot(gs[0, :])     # first row span 2 columns
        x_main = data.index
        y_main = data['Amount']

        # smoothing
        x_smooth = np.linspace(x_main.min(), x_main.max(), 400)
        if len(x_main) > 2:
            slp = make_interp_spline(x_main, y_main, k=2)
            y_smooth = slp(x_smooth)
            ax_main.plot(x_smooth, y_smooth, color="#00e5ff", linewidth=2.2, alpha=0.9)
        else:
            ax_main.plot(x_main, y_main, color="#00e5ff", linewidth=2.2)

        # scatter points
        ax_main.scatter(x_main, y_main, zorder=3, color='#ff5252', marker='o', s=28, edgecolor="white", linewidth=0.5)

        # titles and labels
        ax_main.set_title('PORTFOLIO OVERVIEW', fontweight='bold', fontsize=15, color='#00e5ff', pad=12)
        ax_main.set_ylabel('AMOUNT (PHP)', fontweight='semibold', fontsize=11, color='white', labelpad=8)

        # x-axis labels
        x_main_labels = [f'Q{val}' for val in data['Pay-out']]
        ax_main.set_xticks(x_main, labels=x_main_labels, fontsize=9, color="#bbbbbb")

        # year annotations
        for year in data['Year'].unique():
            position = x_main[data['Year'] == year]
            mid = position.values.mean()
            ax_main.text(mid, -0.12, f'Year {year}', ha='center', va='top',
                         transform=ax_main.get_xaxis_transform(),
                         fontsize=9, color="#888888")

        # vertical separators
        for year in data['Year'].unique()[1:]:  
            pos = x_main[data['Year'] == year].min() - 0.5
            ax_main.axvline(pos, color="white", linestyle="--", alpha=0.15)

        # grid & y-axis formatting
        ax_main.grid(True, linestyle="--", alpha=0.15)
        ax_main.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))

        # ----------------------- dividends per quarter --------------------------------------
        ax_1 = fig.add_subplot(gs[1, 0])
        ax_1.bar(data.index, data['Dividends'], 
                 color="#2ecc71", edgecolor="white", linewidth=0.3, alpha=0.9)

        ax_1.set_title('DIVIDEND GROWTH', fontweight='bold', fontsize=12, color='#00e5ff', pad=10)
        ax_1.set_ylabel('DIVIDENDS (PHP)', fontweight='semibold', fontsize=10, color='white', labelpad=8)

        ax_1_labels = [f'Q{val}' for val in data['Pay-out']]
        ax_1.set_xticks(data.index, ax_1_labels, fontsize=8, color="#bbbbbb")

        for year in data['Year'].unique():
            position = data.index[data['Year'] == year]
            mid = position.values.mean()
            ax_1.text(mid, -0.12, f'Year {year}', ha='center', va='top',
                      transform=ax_1.get_xaxis_transform(),
                      fontsize=8, color="#999999")
            
        # vertical separators
        for year in data['Year'].unique()[1:]:  
            pos = data.index[data['Year'] == year].min() - 0.5
            ax_1.axvline(pos, color="white", linestyle="--", alpha=0.35,  linewidth=0.6)

        ax_1.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:,.0f}'))
        ax_1.grid(True, linestyle="--", alpha=0.15)

        # ----------------------- portfolio composition --------------------------------------
        ax_2 = fig.add_subplot(gs[1, 1])

        div = data['Dividends'].sum()
        capital = data.iloc[-1, data.columns.get_loc('Amount')] - div
        sizes = [div, capital]
        labels = ['Dividends', 'Capital Growth']
        colors = ['#ff7675', '#3498db']

        wedges, texts, autotexts = ax_2.pie(
            sizes, labels=labels, autopct='%1.2f%%',
            startangle=120, counterclock=False,
            colors=colors, shadow=False, explode=(0.05, 0),
            textprops={'color': "white", 'fontsize': 9, 'fontweight': 'bold'}, 
            wedgeprops={'edgecolor': '#1e1e1e', 'linewidth': 1}
)

        ax_2.set_title('PORTFOLIO COMPOSITION', fontweight='bold', fontsize=12, color='#00e5ff', pad=10)

        # layout adjustments
        fig.subplots_adjust(
            top=0.92,      # leave room for titles
            bottom=0.08,   # space below x-axis labels
            left=0.08,     # margin for y-axis labels
            right=0.95,    # space on the right
            hspace=0.35,   # vertical spacing between rows
            wspace=0.3     # horizontal spacing between bottom panels
        )
        
        # save graph
        new_filename = filename.replace('data/', 'data/graph/', 1).replace('.csv', '.png', 1)
        plt.savefig(new_filename, dpi=300)


        if show:
            plt.show()
            print(f"Graph displayed and saved: {new_filename}")
        else:
            print(f"Graph saved (not displayed): {new_filename}")