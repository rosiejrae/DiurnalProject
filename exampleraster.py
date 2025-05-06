Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

# Assuming 'all16AdjSpikes' is your DataFrame
result = all16AdjSpikes.copy()

# Define colors
blue = (0, 0, 1)  # For 'D'
red = (1, 0, 0)   # For 'X'

# Get unique unitIDs for 'D' and 'X'
D_units = result.loc[result['lightCycle'] == 'D', 'unitID'].unique()
... X_units = result.loc[result['lightCycle'] == 'X', 'unitID'].unique()
... 
... # Randomly select 1 from each group if not empty
... random.seed()  # Ensures randomness
... if len(D_units) > 0:
...     D_units = [random.choice(D_units)]
... if len(X_units) > 0:
...     X_units = [random.choice(X_units)]
... 
... # Combine selected units
... combined_units = D_units + X_units
... count_units = len(combined_units) + 1
... 
... # Plot
... plt.figure(figsize=(10, 6))
... for i, unit in enumerate(combined_units, start=1):
...     unit_data = result[result['unitID'] == unit]
...     timestamps = unit_data['adjustedTimestamp'] / 60  # Convert to minutes
...     light_cycle = unit_data['lightCycle'].iloc[0]
... 
...     color = blue if light_cycle == 'D' else red
...     plt.scatter(timestamps, [i] * len(timestamps), color=color, marker='|', s=1000)
... 
... # Add vertical lines
... for x in [15, 20, 45]:
...     plt.axvline(x=x, color='k', linewidth=1.5)
... 
... # Axes settings
... plt.xlabel('Time (min)')
... plt.ylabel('Unit')
... plt.xlim(0, 50)
... plt.ylim(1, count_units - 1)
... plt.yticks(ticks=np.arange(1, len(combined_units)+1), labels=[str(u) for u in combined_units])
... plt.gca().invert_yaxis()  # Match MATLAB's 'YDir', 'reverse'
... 
... plt.tight_layout()
... plt.show()
