Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Assuming 'all16AdjSpikes' is your DataFrame
result = all16AdjSpikes

# Define colors
orange = (1, 0.5, 0)
blue = (0, 0, 1)
red = (1, 0, 0)
dark_green = (0, 0.5, 0)
dark_red = (0.5, 0, 0)

# Separate units by lightCycle
L_units = result.loc[result['lightCycle'] == 'L', 'unitID'].unique()
D_units = result.loc[result['lightCycle'] == 'D', 'unitID'].unique()
... X_units = result.loc[result['lightCycle'] == 'X', 'unitID'].unique()
... 
... # Combine units in desired order
... combined_units = list(L_units) + list(D_units) + list(X_units)
... count_units = len(combined_units) + 1
... 
... # Plot
... plt.figure(figsize=(10, 8))
... for i, unit in enumerate(combined_units, start=1):
...     unit_data = result[result['unitID'] == unit]
...     unit_timestamps = unit_data['adjustedTimestamp'] / 60  # Convert to minutes
...     light_cycle = unit_data['lightCycle'].iloc[0]
... 
...     if light_cycle == 'L':
...         color = orange
...     elif light_cycle == 'D':
...         color = blue
...     elif light_cycle == 'X':
...         color = red
... 
...     plt.scatter(unit_timestamps, [i] * len(unit_timestamps), color=color, marker='|', s=20)
... 
... # Vertical lines
... plt.axvline(x=15, color=dark_green, linewidth=1.5)
... plt.axvline(x=20, color='r', linewidth=1.5)
... plt.axvline(x=45, color='k', linewidth=1.5)
... 
... # Axis labels and formatting
... plt.xlabel('Time (min)')
... plt.ylabel('Unit')
... plt.xlim(0, 50)
... plt.ylim(1, count_units - 1)
... plt.yticks(ticks=np.arange(1, len(combined_units)+1), labels=[str(u) for u in combined_units])
... plt.gca().invert_yaxis()  # Match MATLAB's 'YDir', 'reverse'
... 
... plt.tight_layout()
... plt.show()
