import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

nflx = pd.read_csv('Netflix Stocks Capstone/NFLX.csv')
#print(nflx.head())
dates = nflx['Date'].tolist()
close = nflx['Close'].tolist()
volume = nflx['Volume'].tolist()

plt.subplot(1, 2, 1)
plt.plot(dates, close)
#ax = plt.subplot()
plt.subplot(1, 2, 2)
plt.plot(dates, volume)

plt.show()