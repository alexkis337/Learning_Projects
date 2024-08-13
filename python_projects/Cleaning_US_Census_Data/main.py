import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

# remove max width of columns
pd.set_option('display.max_columns', None)

# concatenate all files in one using glob
files = glob.glob('states*.csv')

df_list = []
for filename in files:
    data = pd.read_csv(filename)
    df_list.append(data)
us_census = pd.concat(df_list, ignore_index=True).reset_index(drop=True)
us_census.drop(columns=['Unnamed: 0'], inplace=True)
us_census.to_csv('us_census.csv', index=False)

print(us_census.info())
# removing $ and converting to float
us_census['Income'] = us_census['Income'].replace('[\$,]', '', regex=True)
us_census['Income'] = us_census['Income'].astype(float)

# splitting GenderPop into MalePop and FemalePop
us_census[['MalePop', 'FemalePop']] = us_census['GenderPop'].astype(str).replace('[MF]', '', regex=True).\
    str.split('_', expand=True)
us_census['MalePop'] = us_census['MalePop'].astype(int)

# FemalePop has some empty values, so we will replace them with the mean of the column
# we replace empty with Nan, then calculate the mean of the column and round it up and replace the Nan with the mean
us_census['FemalePop'] = us_census['FemalePop'].replace(' ', '').apply(lambda x: np.nan if len(x) < 1 else x)

female_mean = int(np.ceil(np.mean(us_census['FemalePop'].dropna().astype(int))))
us_census['FemalePop'] = us_census['FemalePop'].fillna(female_mean).astype(int)

us_census.drop(columns=['GenderPop'], inplace=True)
us_census.drop_duplicates(inplace=True)

print(len(us_census))

x_values = us_census['State']
y_values = us_census['Income']
sizes_m = us_census['MalePop']/100000


plt.scatter(x_values, y_values, s=sizes_m, color='blue', edgecolors='black')

plt.xticks(rotation=90)
plt.legend('MalePop',  loc='upper right')

plt.show()