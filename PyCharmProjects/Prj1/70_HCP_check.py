import pandas as pd

all = pd.read_csv('data_to_check.csv')
hcps = pd.read_csv('data_to_check_70.csv')

hcps['duplicate'] = hcps.apply((lambda row: 'duplicate' if row['lastnames'].upper() in all['Last Name'].tolist() else ''), axis=1)

hcps.to_excel('output.xlsx')