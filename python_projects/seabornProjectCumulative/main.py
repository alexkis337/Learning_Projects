from matplotlib import pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns


df = pd.read_csv('kiva_data.csv')
#print(df.head())
f, ax = plt.subplots(figsize=(15, 10))
sns.violinplot(data=df, x="country", y = "loan_amount")

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

plt.show()