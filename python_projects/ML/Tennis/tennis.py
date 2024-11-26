import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression



# 'Player'
# 'Year'
# 'FirstServe'
# 'FirstServePointsWon'
# 'FirstServeReturnPointsWon'
# 'SecondServePointsWon'
# 'SecondServeReturnPointsWon'
# 'Aces'
# 'BreakPointsConverted'
# 'BreakPointsFaced'
# 'BreakPointsOpportunities'
# 'BreakPointsSaved'
# 'DoubleFaults'
# 'ReturnGamesPlayed'
# 'ReturnGamesWon'
# 'ReturnPointsWon'
# 'ServiceGamesPlayed'
# 'ServiceGamesWon'
# 'TotalPointsWon'
# 'TotalServicePointsWon'
# 'Wins'
# 'Losses'
# 'Winnings'
# 'Ranking


# pd.set_option('display.max_columns', None)
df = pd.read_csv('tennis_stats.csv')
print(df.columns)

m1 = LinearRegression()
x1 = df[['Wins']]
y1 = df[['Winnings']]

x_train, x_test, y_train, y_test = train_test_split(x1, y1, train_size = 0.8, test_size = 0.2, random_state=6)

m1.fit(x1, y1)
y1_pred = m1.predict(x1)

print(m1.score(x1, y1))

plt.scatter(x1, y1, color='blue', alpha=0.6)
plt.plot(x1, y1_pred, color='red')

# plt.scatter(x1, y1, color='blue', alpha=0.6)
# plot a chart of all features in pairs

# plt.scatter(df['Winnings'], df['Losses'])
plt.show()


