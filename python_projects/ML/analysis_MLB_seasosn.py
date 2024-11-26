import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('baseball_reference_2016_clean.csv')

# main columns:
# game_type — is the game during the day or at night
# day_of_week — what day of the week did the game occur
# temperature — average game temperature (Fahrenheit)
# sky — description of sky condition at the time of the game
# total_runs — total runs scored in the game

# pd.set_option('display.max_columns', None)
# print(df.dtypes)

# print(df['attendance'].value_counts(dropna=False), '\n')
# print(df['temperature'].value_counts(dropna=False))

# 1 game type
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='game_type', palette="Set2")
plt.title("Game Type Distribution")
# significantly more night games probably due to the fact that most people work during the day
# and due to big number of games over the year and inability to play all of them during the weekend

# 2 order by day of the week on the chart
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=days, ordered=True)
df = df.sort_values('day_of_week')
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='day_of_week', palette="Set2")
plt.title("Games by Day of the Week")
# Monday and Thursday are the days when the least games are played.
# assume Monday low due to be 1st day of work week + post-weekend fatigue
# Thursday because people prefer to save energy for Friday

# 3 Sky Condition
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='sky', palette="Set2")
plt.title("Sky Condition during Games")
# absolutely random

# 4 building a heatmap of attendance over temperature
plt.figure(figsize=(10, 6))
plt.hist2d(df['temperature'].fillna(df['temperature'].mean()), df['attendance'].fillna(df['attendance'].mean()),
           bins=(10, 10), cmap='hot')
plt.colorbar()
plt.xlabel('Temperature')
plt.ylabel('Attendance')
plt.title('Attendance over Temperature')
# no clear correlation between temperature and attendance

# 5 wins by sky condition
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='sky', y='home_team_win', palette="Set2")
plt.title("Home Team Wins by Sky Condition")
# no clear correlation between sky condition and home team wins, higher dispersion for low-data categories

# 6 temperature
plt.figure(figsize=(12, 6))
sns.histplot(df['temperature'], bins=20, kde=True)
plt.title("Temperature Distribution")
# median temperature is around 70 degrees

# 7 wins by temperature
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='temperature', y='home_team_win', palette="Set2")
plt.title("Impact of Temperature on Home Team Wins")
plt.show()
# as most of the games are played in the temperature range of 60-90 degrees, the win rate is around 0.5
# data on the sides of the chart is more fluctuating due to the low number of games played in those temperature ranges
