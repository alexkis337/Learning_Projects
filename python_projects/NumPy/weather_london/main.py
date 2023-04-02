import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import pyplot


pd.set_option('display.max_columns', None)
london_data = pd.read_csv('data.csv')
london_data = london_data.iloc[:250]
temp = london_data['TemperatureC']

print(london_data.head())
# print(len(london_data))
# print(temp)

average_temp = np.mean(temp)
temp_var = np.var(temp)
temp_std = np.std(temp)
# print('avg_temp is ', average_temp)
# print('temp_var is', temp_var)
# print('std is ', temp_std)

january = london_data.loc[london_data['month'] == 1]
june, july = (london_data.loc[london_data['month'] == 6], london_data.loc[london_data['month'] == 7])
# print(np.std(june), np.std(july))

plt.plot(london_data['DateUTC'], london_data['Humidity'])
plt.show()

