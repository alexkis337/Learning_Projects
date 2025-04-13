# techland interview

import matplotlib.pyplot as plt
import pandas as pd

# creating data
data = {
    'weapon': ['@knife01', '@sword01', '@bow13', '@club01', '@unicornmagicpistol37'],
    'perk_noperk': [0, 0, 0, 3, 0],
    'perk_speed': [3, 2, 2, 0, 3],
    'perk_damage': [5, 3, 5, 0, 5],
    'perk_range': [1, 5, 1, 0, 1],
    'perk_legendary': [0, 0, 0, 0, 1]
}



df = pd.DataFrame(data)
df.set_index('weapon', inplace=True)
df.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))

# y limit set for more visual appeal so legend doesn't overlap with the bars
plt.ylim(0, 15)
plt.title('Weapon Perks Distribution', fontsize=16)
plt.xlabel('Weapon', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.legend(title='Perk', loc='upper right')
plt.xticks(rotation=45)

# Show the plot
plt.show()