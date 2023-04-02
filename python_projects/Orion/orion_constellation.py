import pandas as pd

x = pd.read_csv('crm_nov_backup.csv')
x.to_csv('crm_nov_cos_backup.csv')