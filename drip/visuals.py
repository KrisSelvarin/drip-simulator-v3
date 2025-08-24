# for graph generation
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Visuals:
    
    @staticmethod
    def graph(filename):
        """Generates Graph"""
        data = pd.read_csv(filename)

        # graph
        fig, ax = plt.subplots(figsize=(7,4))
        ax.plot(data.index, data['Amount'], marker='o')
        ax.set_title('PORTFOLIO OVERVIEW', fontweight='bold')

        # x-axis (Quarters)
        x_label = [f"Q{val}" for val in data['Pay-out']]
        ax.set_xticks(data.index, x_label, fontsize=8)

        # x-axis (years)
        for year in data['Year'].unique():
            position = data.index[data['Year'] == year]
            mid = position.values.mean()
            Year = f'Year {year}'
            ax.text(mid, -0.1, Year, ha='center', va='top', fontweight='semibold',
                    transform=ax.get_xaxis_transform())
            
        # y-axis (Amount)
        ticks = np.linspace(data['Amount'].min(), data['Amount'].max(), 8)
        y_labels = [f'{val:,.2f}' for val in ticks]
        ax.set_yticks(ticks, y_labels)
        ax.set_ylabel('PORTFOLIO VALUE (PHP)', fontweight='semibold')
            
        plt.tight_layout()
        plt.show()