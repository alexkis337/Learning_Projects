import pandas as pd

df = pd.read_csv('TEST.csv')
df['Overall score shift'] = df.apply('=VLOOKUP(B2;$B$2:$D$50;3;FALSE', inplace=True)

print(df.head())