import requests
import numpy as np
import pandas as pd
from loc_address import get_coordinates, get_location

pd.options.display.max_columns = 9
df = pd.read_excel('C:/Users/Oleksandr/Desktop/final_coords.xlsx')

try:
    df['address_coord'] = df['address_coord'].apply(lambda x: x.replace('(', ''))
    df['address_coord'] = df['address_coord'].apply(lambda x: x.replace(')', ''))
    df['address_coord'] = df['address_coord'].apply(lambda x: x.split(','))

    df['hco_coord'] = df['hco_coord'].apply(lambda x: x.replace('(', ''))
    df['hco_coord'] = df['hco_coord'].apply(lambda x: x.replace(')', ''))
    df['hco_coord'] = df['hco_coord'].apply(lambda x: x.split(','))
except AttributeError:
    pass

def look_func(address, hcos):
    for hospital in hcos:
        try:
            if np.sqrt((float(address[0].strip()) - float(hospital[0].strip()))**2 +
                       (float(address[1].strip()) - float(hospital[1].strip()))**2) < 0.0055:
                return hospital
        except:
            pass




# print(type(df['address_coord'][1]))
# print(type(df['hco_coord'][1]))

df['suggested_hco'] = df.apply(lambda row: look_func(row['address_coord'], df['hco_coord']), axis=1)

df2 = df[['organisation_name', 'hco_coord']]

df.to_excel('C:/Users/Oleksandr/Desktop/final_sug_hco.xlsx')
#print(df.head())
